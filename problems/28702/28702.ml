module FizzBuzz = struct
  type t = Fizz | Buzz | Both | None of int

  let to_string = function
    | Fizz -> "Fizz"
    | Buzz -> "Buzz"
    | Both -> "FizzBuzz"
    | None num -> Int.to_string num

  let of_string = function
    | "Fizz" -> Fizz
    | "Buzz" -> Buzz
    | "FizzBuzz" -> Both
    | raw -> None (int_of_string raw)
end

let fizzbuzz i =
  if i mod 3 == 0 && i mod 5 == 0 then FizzBuzz.Both
  else if i mod 3 == 0 then FizzBuzz.Fizz
  else if i mod 5 == 0 then FizzBuzz.Buzz
  else FizzBuzz.None i

let next first second third =
  match third with
  | FizzBuzz.None num -> fizzbuzz (num + 1)
  | _ -> (
      match second with
      | FizzBuzz.None num -> fizzbuzz (num + 2)
      | _ -> (
          match first with
          | FizzBuzz.None num -> fizzbuzz (num + 3)
          | _ -> FizzBuzz.None (-1)))

let main =
  let first = FizzBuzz.of_string (read_line ()) in
  let second = FizzBuzz.of_string (read_line ()) in
  let third = FizzBuzz.of_string (read_line ()) in
  next first second third
  |> FizzBuzz.to_string
  |> print_endline
