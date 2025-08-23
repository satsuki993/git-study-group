import requests
import hashlib

def get_github_file_sha256(url):
    """
    指定されたGitHubのRAWファイルURLからSHA-256ハッシュ値を計算します。
    """
    try:
        # GitHubのRAWファイルURLから内容を取得
        response = requests.get(url)
        response.raise_for_status()  # HTTPエラーがあれば例外を発生させる

        # SHA-256ハッシュオブジェクトを作成
        sha256_hash = hashlib.sha256()

        # ファイルの内容をハッシュオブジェクトにアップデート
        sha256_hash.update(response.content)

        # 16進数形式のハッシュ値を取得して返す
        return sha256_hash.hexdigest()

    except requests.exceptions.RequestException as e:
        print(f"エラー: ファイルのダウンロードに失敗しました - {e}")
        return None

# 使用例
github_raw_url = "https://github.com/satsuki993/git-study-group/blob/develop/tree_test/tree_test2/tree_test2.txt"
sha256_value = get_github_file_sha256(github_raw_url)

if sha256_value:
    print(f"ファイルURL: {github_raw_url}")
    print(f"SHA-256ハッシュ値: {sha256_value}")