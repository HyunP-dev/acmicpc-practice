let print_times_table n = 
  List.init 9 (fun x -> x + 1)
   |> List.map (fun r -> Format.sprintf "%d * %d = %d\n" n r (n * r))
   |> List.iter print_string

let _ = print_times_table (read_int ())
