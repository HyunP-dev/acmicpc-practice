let count_hole ch = match ch with
 | 'a' | 'b' | 'd' | 'e' | 'g' | 'o' | 'p' | 'q'
 | 'A' | 'D' | 'O' | 'P' | 'Q' | 'R' | '@' -> 1
 | 'B' -> 2
 | _ -> 0

let _ = read_line ()
 |> String.to_seq
 |> Seq.map count_hole
 |> Seq.fold_left (+) 0
 |> print_int
