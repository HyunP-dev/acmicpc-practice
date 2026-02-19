let id = fun x -> x

let encode ch = Char.code ch - Char.code 'a' + 1

let rec modpow n k m = 
  let rec loop k acc =
    match k with
    | 0 -> acc
    | _ -> loop (k - 1) ((n * acc) mod m)
  in
    loop k 1

let hash a r m =
  List.init (String.length a) (fun i -> 
    (((encode (String.get a i)) mod m) * (modpow r i m)) mod m)
  |> List.fold_left (fun acc r -> (acc + r) mod m) 0

let main =
  let l = read_int () in
  let a = read_line () in
  Printf.printf "%d\n" (hash a 31 1234567891)
