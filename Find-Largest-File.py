import os

def find_largest_file(directory):
    """
    Recursively traverses the specified directory and returns the largest file found.

    Args:
        directory (str): The path of the directory to traverse.

    Returns:
        tuple: A tuple containing the path of the largest file and its size in bytes.
               If no files are found, returns (None, 0).
    """
    largest_file = None
    largest_size = 0
    
    # 지정된 경로를 재귀적으로 순회
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                # 파일 크기를 확인
                size = os.path.getsize(filepath)
                if size > largest_size:
                    largest_size = size
                    largest_file = filepath
            except OSError as e:
                print(f"Error accessing file {filepath}: {e}")
    
    return largest_file, largest_size

# 사용 예시
if __name__ == "__main__":
    directory = input("탐색할 경로를 입력하세요: ").strip()
    largest_file, largest_size = find_largest_file(directory)
    
    if largest_file:
        print(f"가장 큰 파일: {largest_file}")
        print(f"파일 크기: {largest_size} 바이트")
    else:
        print("지정된 경로에 파일이 없거나 접근할 수 없습니다.")
