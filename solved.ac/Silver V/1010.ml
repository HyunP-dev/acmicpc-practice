let rec factorial n = match n with
 | 0 | 1 -> 1
 | 2 -> 2
 | _ -> n * factorial (n - 1)

let perm n k = factorial n / factorial (n - k)

let comb n k = perm n k / factorial k

let solve a b = comb b a

let _ = List.init (read_int ()) (fun _ -> Scanf.scanf "%d %d\n" solve)
 |> List.iter (fun answer -> print_string (Format.sprintf "%d\n" answer))
