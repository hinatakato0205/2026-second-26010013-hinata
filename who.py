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
    print("-----outputのなかみ-----")
    print(output)
    lines = output.splitlines()
    #print(f"インデックス指定で表示{lines[0]}")
    print()
    print("行ごとに分けてリストにしたもの")
    print(lines)
    print()

    #ミッション4 ミッション5
    session_count = len(lines)

    if session_count==0:
        print("ログインセッションなし")

    else:
        print(f"ログインセッション数は{session_count}です。")

    print()

    users = []
    #ミッション6
    for line in lines:
        parts = line.split()

        if parts[-1] in users:
            continue

        print(f"1行ごとに表示{line}")
        print()
        print(f"1行の要素を分解して表示{parts}")
        print()
        username = parts[0]
        print(f"ユーザー名の場所を指定する{username}")
        users.append(parts[-1])

    print()
    print(f"ログインユーザー数は{len(users)}です。")
    print(users)

except FileNotFoundError:
    print("コマンドが見つかりません")

#実行結果のコードは0で成功。それ以外はエラー
