let is_square n = (fun r -> r * r = n)(int_of_float (sqrt (float_of_int n)))
let is_symmetry_square n = is_square n &&
  string_of_int n
  |> String.to_seq
  |> List.of_seq
  |> List.rev
  |> List.to_seq
  |> String.of_seq
  |> int_of_string
  |> is_square


let _ = List.init (read_int()) (fun _ -> is_symmetry_square(read_int()))
 |> List.iter (fun is_ss -> print_string (Format.sprintf "%s\n" (if is_ss then "YES" else "NO")))
