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
    print(f"インデックス指定で表示{lines[0]}")

    print(lines)
    

    #ミッション4 ミッション5
    session_count = len(lines)

    if session_count==0:
        print("ログインセッションなし")

    else:
        print(f"ログインセッション数は{session_count}です。")

    #ミッション6
    for line in lines:
        print(line)

except FileNotFoundError:
    print("コマンドが見つかりません")

#実行結果のコードは0で成功。それ以外はエラー
