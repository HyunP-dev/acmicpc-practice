let read_inputs n =
  let rec loop n m =
    match n with
    | 0 -> m
    | _ ->
        loop (n - 1)
          (let e = read_int () in
           let count =
             match Hashtbl.find_opt m e with Some c -> c | None -> 0
           in
           Hashtbl.replace m e (count + 1);
           m)
  in
  loop n (Hashtbl.create 10000)

let main =
  let n = read_int () in
  let m = read_inputs n in
  Hashtbl.to_seq_keys m |> List.of_seq
  |> List.sort Stdlib.compare
  |> List.iter (fun e ->
      let count = Hashtbl.find m e in
      for i = 1 to count do
        Printf.printf "%d\n" e
      done)
