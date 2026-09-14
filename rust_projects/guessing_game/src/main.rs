use std::io;

fn main() {
    println!("数を当ててください");          // 数を当ててごらん

    println!("予想を入力してね");   // ほら、予想を入力してね

    let mut guess = String::new();

    io::stdin()
        .read_line(&mut guess)
        .expect("行の読み込みに失敗しました");     // 行の読み込みに失敗しました

    println!("次のように予想しました: {guess}");       // 次のように予想しました: {guess}
}