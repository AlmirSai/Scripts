#!/usr/bin/env python3

import os
import platform
import subprocess
import glob
import argparse
import time

from pathlib import Path
from typing import List, Optional, Tuple


class PlatformConfig:
    def __init__(self):
        self.system = platform.system().lower()
        self.is_windows = self.system == 'windows'
        self.is_linux = self.system == 'linux'
        self.is_macos = self.system == 'darwin'
        self.default_compilers = {
            'windows': ['cl', 'g++', 'clang++'],
            'linux': ['g++', 'clang++'],
            'darwin': ['clang++', 'g++']
        }
        self.make_commands = {
            'windows': ['nmake', 'mingw32-make', 'make'],
            'linux': ['make'],
            'darwin': ['make']
        }
        self.executable_extension = '.exe' if self.is_windows else ''

    def get_available_compilers(self) -> List[str]:
        """Get list of available compilers for current platform."""
        available = []
        for compiler in self.default_compilers.get(self.system, []):
            if self.is_compiler_available(compiler):
                available.append(compiler)
        return available

    def is_compiler_available(self, compiler: str) -> bool:
        """Check if a compiler is available in the system."""
        try:
            if self.is_windows and compiler == 'cl':
                # Check for MSVC compiler
                result = subprocess.run(
                    ['cl'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                return result.returncode == 0
            else:
                result = subprocess.run(
                    [compiler, '--version'],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                return result.returncode == 0
        except FileNotFoundError:
            return False

    def get_make_command(self) -> Optional[str]:
        """Get the appropriate make command for the current platform."""
        for cmd in self.make_commands.get(self.system, []):
            try:
                subprocess.run(
                    [cmd, '--version'],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                return cmd
            except FileNotFoundError:
                continue
        return None


class BuildConfig:
    def __init__(self, build_type: str = "Debug",
                 compiler: str = "",
                 cpp_standard: str = "20",
                 generate_assembly: bool = True,
                 platform_config: Optional[PlatformConfig] = None):
        self.platform = platform_config or PlatformConfig()
        self.build_type = build_type
        self.build_dir = f"build_{build_type.lower()}"
        self.cpp_standard = cpp_standard
        self.generate_assembly = generate_assembly

        # Set default compiler based on platform if not specified
        available_compilers = self.platform.get_available_compilers()
        self.compiler = compiler if compiler else (available_compilers[0] if available_compilers else "g++")

    def get_cmake_generator(self) -> Optional[str]:
        """Get the appropriate CMake generator for the current platform and compiler."""
        if self.platform.is_windows:
            if self.compiler == 'cl':
                return "NMake Makefiles"
            elif self.compiler in ['g++', 'clang++']:
                return "MinGW Makefiles"
        return None


def create_directories():
    """Create necessary directories if they don't exist."""
    directories = ['src/atomic', 'tests']
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)


def list_cpp_files() -> List[str]:
    """List all available C++ files in the project."""
    cpp_files = glob.glob('src/**/*.cpp', recursive=True)
    return [f for f in cpp_files if os.path.isfile(f)]


def clean_build_directories():
    """Clean all build directories."""
    build_dirs = glob.glob('build_*')
    for build_dir in build_dirs:
        if os.path.isdir(build_dir):
            try:
                if platform.system() == 'Windows':
                    subprocess.run(
                        ['rmdir', '/s', '/q', build_dir], check=True)
                else:
                    subprocess.run(['rm', '-rf', build_dir], check=True)
                print(f"Cleaned {build_dir}")
            except subprocess.CalledProcessError as e:
                print(f"Error cleaning {build_dir}: {e}")


def build_and_run(cpp_file: str, config: BuildConfig):
    """Build and run the selected C++ file with specified configuration."""
    start_time = time.time()
    build_stats = {}
    try:
        print(f"\nStarting build process for {cpp_file}...")
        print(f"Configuration:")
        print(f" - Build Type: {config.build_type}")
        print(f" - Compiler: {config.compiler}")
        print(f" - C++ Standard: {config.cpp_standard}")
        print(f" - Assembly Generation: {'Enabled' if config.generate_assembly else 'Disabled'}")
        
        # Update CMakeLists.txt
        cmake_start = time.time()
        with open('CMakeLists.txt', 'w') as f:
            f.write('cmake_minimum_required(VERSION 3.10)\n')
            f.write('project(AtomicExample)\n\n')
            f.write(f'set(CMAKE_CXX_STANDARD {config.cpp_standard})\n')
            f.write('set(CMAKE_CXX_STANDARD_REQUIRED True)\n')

            # Add sanitizer and safety flags
            if not config.platform.is_windows:
                f.write('set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Wpedantic")\n')
                if config.build_type == "Debug":
                    f.write('set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fsanitize=address,undefined -fno-omit-frame-pointer")\n')
                    f.write('set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -fsanitize=address,undefined")\n')

            if config.platform.is_windows and config.compiler == 'cl':
                f.write('set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /EHsc /W4")\n')
            elif config.generate_assembly:
                f.write('set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -S")\n')

            if config.compiler:
                f.write(f'set(CMAKE_CXX_COMPILER {config.compiler})\n\n')

            f.write(f'add_executable(main {cpp_file})\n')

        build_stats['cmake_config_time'] = time.time() - cmake_start
        print(f"\nCMake configuration completed in {build_stats['cmake_config_time']:.2f} seconds")

        # Create build directory and run cmake
        os.makedirs(config.build_dir, exist_ok=True)
        os.chdir(config.build_dir)

        # Run cmake with build type and generator
        cmake_gen_start = time.time()
        cmake_args = ['cmake', '..']
        if generator := config.get_cmake_generator():
            cmake_args.extend(['-G', generator])
            print(f"Using CMake generator: {generator}")
        cmake_args.append(f'-DCMAKE_BUILD_TYPE={config.build_type}')

        print("\nGenerating build files...")
        subprocess.run(cmake_args, check=True)
        build_stats['cmake_generate_time'] = time.time() - cmake_gen_start
        print(f"Build files generated in {build_stats['cmake_generate_time']:.2f} seconds")

        # Run make/build command
        if make_cmd := config.platform.get_make_command():
            make_start = time.time()
            print(f"\nBuilding with {make_cmd}...")
            make_args = [make_cmd]
            if make_cmd == 'make':
                make_args.append(f'-j{os.cpu_count() or 2}')
            subprocess.run(make_args, check=True)
            build_stats['build_time'] = time.time() - make_start
            print(f"Build completed in {build_stats['build_time']:.2f} seconds")

        # Check for assembly output if requested
        if config.generate_assembly:
            assembly_files = glob.glob('CMakeFiles/main.dir/*.s')
            if assembly_files:
                print("\nAssembly files generated:")
                for asm_file in assembly_files:
                    print(f" - {asm_file}")
                    asm_size = os.path.getsize(asm_file)
                    print(f"   Size: {asm_size/1024:.2f} KB")

        # Run the executable
        print(f"\nExecuting {cpp_file}...")
        executable = f"./main{config.platform.executable_extension}"
        run_start = time.time()
        process = subprocess.run([executable], check=True, capture_output=True, text=True)
        run_time = time.time() - run_start

        # Print execution results
        print("\nExecution Results:")
        print(f"Time taken: {run_time:.3f} seconds")
        if process.stdout:
            print("\nProgram Output:")
            print(process.stdout)

        # Print final statistics
        total_time = time.time() - start_time
        print("\nBuild and Execution Statistics:")
        print(f" - CMake Configuration: {build_stats['cmake_config_time']:.2f} seconds")
        print(f" - CMake Generation: {build_stats['cmake_generate_time']:.2f} seconds")
        print(f" - Build Time: {build_stats.get('build_time', 0):.2f} seconds")
        print(f" - Execution Time: {run_time:.3f} seconds")
        print(f" - Total Time: {total_time:.2f} seconds")

    except subprocess.CalledProcessError as e:
        print(f"\nError during build/run process: {e}")
        if e.output:
            print("Error output:")
            print(e.output)
        raise
    finally:
        os.chdir('..')


def run_tests(config: BuildConfig):
    """Run all available tests in the project."""
    cpp_files = glob.glob('src/**/*_test.cpp', recursive=True)
    if not cpp_files:
        print("No test files found.")
        return

    print("\nRunning tests...")
    failed_tests = []
    passed_tests = []
    test_stats = {}
    total_start_time = time.time()

    for test_file in cpp_files:
        try:
            print(f"\nExecuting test: {test_file}")
            test_start_time = time.time()
            build_and_run(test_file, config)
            test_time = time.time() - test_start_time
            test_stats[test_file] = test_time
            passed_tests.append(test_file)
        except subprocess.CalledProcessError:
            failed_tests.append(test_file)

    total_time = time.time() - total_start_time

    print("\nTest Execution Summary:")
    print(f"Total tests: {len(cpp_files)}")
    print(f"Passed: {len(passed_tests)}")
    print(f"Failed: {len(failed_tests)}")
    print(f"Total time: {total_time:.2f} seconds\n")

    if passed_tests:
        print("Passed Tests:")
        for test in passed_tests:
            print(f" ✓ {test} ({test_stats[test]:.2f}s)")

    if failed_tests:
        print("\nFailed Tests:")
        for test in failed_tests:
            print(f" ✗ {test}")
        return False

    print("\nAll tests passed successfully!")
    return True


def run_linter(cpp_files: List[str]):
    """Run clang-tidy linter on the specified C++ files."""
    try:
        subprocess.run(['clang-tidy', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("clang-tidy not found. Please install clang-tidy to enable linting.")
        return False

    print("\nRunning linter...")
    failed_files = []
    for cpp_file in cpp_files:
        try:
            print(f"\nLinting: {cpp_file}")
            subprocess.run(
                ['clang-tidy', cpp_file, '--', '-std=c++20'],
                check=True,
                capture_output=True,
                text=True
            )
        except subprocess.CalledProcessError as e:
            print(f"Linting errors in {cpp_file}:")
            print(e.output)
            failed_files.append(cpp_file)

    if failed_files:
        print("\nLinting failed for the following files:")
        for file in failed_files:
            print(f" - {file}")
        return False
    print("\nLinting completed successfully!")
    return True


def generate_tests():
    """Generate test files using the test generator."""
    try:
        import test_generator
        test_generator.main()
        print("\nTest files generated successfully!")
    except Exception as e:
        print(f"\nError generating test files: {e}")


def parse_args() -> Tuple[argparse.Namespace, PlatformConfig]:
    """Parse command line arguments and return configuration."""
    platform_config = PlatformConfig()
    available_compilers = platform_config.get_available_compilers()
    default_compiler = available_compilers[0] if available_compilers else "g++"

    parser = argparse.ArgumentParser(
        description='Build and run C++ examples with various configurations.')
    
    parser.add_argument('-t', '--type', choices=['Debug', 'Release'],
                      default='Debug', help='Build type')
    parser.add_argument('-c', '--compiler', default=default_compiler,
                      help=f'Compiler to use (default: {default_compiler})')
    parser.add_argument('-s', '--std', default='20',
                      help='C++ standard to use (default: 20)')
    parser.add_argument('-f', '--file',
                      help='Specific C++ file to build and run')
    parser.add_argument('-a', '--assembly', action='store_true',
                      help='Generate assembly output')
    parser.add_argument('--clean', action='store_true',
                      help='Clean build directories before building')
    parser.add_argument('--lint', action='store_true',
                      help='Run clang-tidy linter on source files')
    parser.add_argument('--run-tests', action='store_true',
                      help='Run all available tests')
    parser.add_argument('--generate-tests', action='store_true',
                      help='Generate test files')

    args = parser.parse_args()
    return args, platform_config


def main():
    args, platform_config = parse_args()
    config = BuildConfig(
        build_type=args.type,
        compiler=args.compiler,
        cpp_standard=args.std,
        generate_assembly=args.assembly,
        platform_config=platform_config
    )

    if args.clean:
        clean_build_directories()
        if not args.file and not args.generate_tests and not args.run_tests:  # If only cleaning was requested
            return

    create_directories()
    
    if args.generate_tests:
        generate_tests()

    cpp_files = list_cpp_files()
    if args.lint:
        if not run_linter(cpp_files):
            print("\nLinting failed. Please fix the issues and try again.")
            return

    if args.run_tests:
        if not run_tests(config):
            print("\nSome tests failed. Please check the output above.")
            return

    if not cpp_files:
        print("No C++ files found in the project.")
        return

    if args.file:
        if args.file in cpp_files:
            print(f"\nBuilding and running: {args.file}")
            build_and_run(args.file, config)
        else:
            print(f"Error: File {args.file} not found in the project.")
            return
    else:
        while True:
            print("\nAvailable C++ files:")
            for i, file in enumerate(cpp_files, 1):
                print(f"{i}. {file}")

            try:
                choice = int(
                    input("\nSelect a file to build and run (0 to exit): ")
                )
                if choice == 0:
                    break
                if 1 <= choice <= len(cpp_files):
                    selected_file = cpp_files[choice - 1]
                    print(f"\nBuilding and running: {selected_file}")
                    build_and_run(selected_file, config)
                else:
                    print("Invalid selection!")
            except ValueError:
                print("Please enter a valid number!")
            except subprocess.CalledProcessError:
                print("Build or run failed. Please check the output above.")
            except KeyboardInterrupt:
                print("\nBuild process interrupted by user.")
                break


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
