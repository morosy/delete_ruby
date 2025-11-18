import re
import sys
import os

def remove_aozora_ruby(input_path):
    """
    指定されたファイルから青空文庫形式のルビ、注釈記号などを削除し、
    _cleaned を付けたファイル名で保存します。
    
    削除対象:
    1. ルビ: 《...》
    2. 入力者注: ［＃...］
    3. ルビ開始記号: ｜
    """
    # 出力ファイル名の生成
    root, ext = os.path.splitext(input_path)
    output_path = f"{root}_cleaned{ext}"

    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            text = f.read()

        # --- 削除処理の実行 ---
        # 1. ルビの削除: 《...》
        text = re.sub(r'《.*?》', '', text)
        # 2. 入力者注の削除: ［＃...］
        text = re.sub(r'［＃.*?］', '', text)
        # 3. ルビ開始記号の削除: ｜
        cleaned_text = re.sub(r'｜', '', text)

        # ----------------------

        # ファイル書き出し
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_text)

        print(f"処理完了: {output_path} を作成しました。")

    except FileNotFoundError:
        print(f"エラー: ファイル '{input_path}' が見つかりません。")
    except UnicodeDecodeError:
        print("エラー: 文字コードが合いません。コード内の encoding='utf-8' を 'shift_jis' (または 'cp932') に変更して試してください。")
    except Exception as e:
        print(f"予期せぬエラーが発生しました: {e}")

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        print("使用法: python remove_ruby.py <ファイルパス>")
    else:
        remove_aozora_ruby(args[1])