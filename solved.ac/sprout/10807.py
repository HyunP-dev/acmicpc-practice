let _ = 
  let n = read_int();
  let a: string list = read_line()
  |> String.split_on_char ' '
  |> List.map Stdlib.int_of_string;
  let v: int = read_int();
  a |> List.filter (fun e: int -> e = v) |> List.;

