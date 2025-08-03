import subprocess
from pathlib import Path
import os

def get_git_object_id(file_path: str) -> str:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        # git hash-object を使ってGitオブジェクトIDを取得
        result = subprocess.run(
            ["git", "hash-object", str(path)],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to get Git object ID: {e.stderr.strip()}")

def get_home_directory() -> str:
    """
    ユーザーのホームディレクトリの絶対パスを文字列で返す関数
    """
    return str(Path.home())

# 使用例
if __name__ == "__main__":
    home_dir = get_home_directory()
    
    file_path = os.path.join(home_dir,"hobbyspace/git-study-group","tree_test/tree_test.txt")
    try:
        git_id = get_git_object_id(file_path)
        print(f"{file_path} のGitオブジェクトID: {git_id}")
    except Exception as e:
        print(e)
