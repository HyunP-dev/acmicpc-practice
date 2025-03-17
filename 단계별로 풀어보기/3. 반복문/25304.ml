let _ = 
  if (compare (read_int ())
    (List.init (read_int ()) (fun _ -> Scanf.scanf "%d %d\n" ( * ))
     |> List.fold_left (+) 0)) = 0 then 
    print_string "Yes"
  else
    print_string "No"
