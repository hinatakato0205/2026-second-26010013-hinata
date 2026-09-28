# use std::io;

# fn main() {
#     println!("Guess the number!");          // 数を当ててごらん

#     println!("Please input your guess.");   // ほら、予想を入力してね

#     let mut guess = String::new();

#     io::stdin()
#         .read_line(&mut guess)
#         .expect("Failed to read line");     // 行の読み込みに失敗しました

#     println!("You guessed: {guess}");       // 次のように予想しました: {guess}
# }

import random

def main():
    while True:
        secret_number = random.randint(1,10)
        print("Guess the number!")

        try:
            guess = int(input("Please input your guess : "))
        except ValueError:
            print("整数を入力してください")
            continue

        print(f'You guessed: {guess}')
        print(f'secret_number: {secret_number}')

        if guess > secret_number:
            print("Too Big!")
            continue
        elif guess < secret_number:
            print("Too Small!")
            continue
        else:
            print("You Win!!")
            break

if __name__ == "__main__":
    main()