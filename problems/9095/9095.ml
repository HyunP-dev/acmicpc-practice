let id = fun x -> x

let rec f = function
  | 1 -> 1 | 2 -> 2 | 3 -> 4
  | n -> f(n - 1) + f(n - 2) + f(n - 3)

let main = 
  let n = Scanf.scanf "%d\n" id in
  List.init n (fun _ -> Scanf.scanf "%d\n" id)
  |> List.map (fun e -> Printf.printf "%d\n" (f e))
