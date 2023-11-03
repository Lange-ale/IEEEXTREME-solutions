use std::collections::{HashMap, HashSet, BTreeMap};
use std::io::{self, BufRead};

fn sum_of_squares(number: i64) -> i64 {
    let mut sum = 0;
    let mut num = number;
    while num > 0 {
        let digit = num % 10;
        sum += digit * digit;
        num /= 10;
    }
    sum
}

fn is_happy(number: i64, happy_map: &mut BTreeMap<i64, bool>, seen_numbers: &mut HashSet<i64>) -> bool {
    let mut num = number;
    let mut cycle = false;

    while num != 1 {
        if let Some(&happy) = happy_map.get(&num) {
            if happy {
                return true;
            } else {
                return false;
            }
        }
        if !seen_numbers.insert(num) {
            cycle = true;
            happy_map.insert(number, false);
            break;
        }
        num = sum_of_squares(num);
    }

    if !cycle {
        happy_map.insert(number, true);
        return true;
    }
    false
}

fn main() {
    let stdin = io::stdin();
    let mut s = String::new();
    stdin.lock().read_line(&mut s).unwrap();
    let values: Vec<i64> = s
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    assert_eq!(values.len(), 2);
    let var1 = values[0];
    let var2 = values[1];
    let mut happy_numbers = 0;
    let mut happy_map = BTreeMap::new();
    let mut seen_numbers = HashSet::new();

    for i in var1..=var2 {
        seen_numbers.clear();
        if is_happy(i, &mut happy_map, &mut seen_numbers) {
            happy_numbers += 1;
        }
    }
    println!("{}", happy_numbers);
}