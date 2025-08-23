import hashlib

def get_file_sha256(file_path):
    """
    指定されたローカルファイルのSHA-256ハッシュ値を計算します。
    """
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            # ファイルをチャンク単位で読み込みながらハッシュを計算
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print(f"エラー: ファイルが見つかりません - {file_path}")
        return None
    except Exception as e:
        print(f"エラー: ハッシュ計算中に問題が発生しました - {e}")
        return None

# 使用例
file_path = "SHA-256/tree_test2.txt"  # 実際のファイルパスに置き換えてください
sha256_value = get_file_sha256(file_path)

if sha256_value:
    print(f"ファイルパス: {file_path}")
    print(f"SHA-256ハッシュ値: {sha256_value}")
