let _ = List.init (Scanf.scanf "%d\n" (fun x -> x)) (fun _ -> Scanf.scanf "%d %d\n" (+))
 |> List.iter (Format.printf "%d\n")
