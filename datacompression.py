import argparse
import zipfile
import os

def compress(input_path, output_path):
    """
    Compresses the input file or directory to a zip file.
    """
    with zipfile.ZipFile(output_path, 'w') as zipf:
        if os.path.isfile(input_path):
            zipf.write(input_path, os.path.basename(input_path))
        elif os.path.isdir(input_path):
            for root, dirs, files in os.walk(input_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, input_path))
        else:
            raise ValueError("Input path does not exist.")

    print(f"Compression successful. Output file: {output_path}")

def decompress(input_path, output_dir):
    """
    Decompresses the input zip file to the specified directory.
    """
    with zipfile.ZipFile(input_path, 'r') as zipf:
        zipf.extractall(output_dir)

    print(f"Decompression successful. Output directory: {output_dir}")

def main():
    """
    Parses command-line arguments and performs compression or decompression.
    """
    parser = argparse.ArgumentParser(description="Compress or decompress files or directories.")
    parser.add_argument("operation", choices=["compress", "decompress"], help="Operation to perform")
    parser.add_argument("input_path", help="Path to the input file or directory")
    parser.add_argument("output_path", help="Path to the output file or directory")

    args = parser.parse_args()

    if args.operation == "compress":
        compress(args.input_path, args.output_path)
    elif args.operation == "decompress":
        decompress(args.input_path, args.output_path)

if __name__ == "__main__":
    main()
