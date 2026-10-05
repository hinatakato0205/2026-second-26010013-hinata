import subprocess

result = ""
try:	
    result = subprocess.run(
    ["who"],
    capture_output=True,
    text=True
	)

    #print(f"標準出力{result.stdout}")
    #print(f"標準エラー出力{result.stderr}")
    #print(f"実行結果{result.returncode}")

    output = result.stdout.strip()
    #print(output)
    lines = output.splitlines()
    print(lines[0])

except FileNotFoundError:
    print("コマンドが見つかりません")

#実行結果のコードは0で成功。それ以外はエラー
