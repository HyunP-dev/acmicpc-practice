let id = function x -> x

let factorize n = 
  let rec loop n d factors = 
    if n == 1 then
      factors
    else if n mod d == 0 then
      loop (n / d) d (d::factors)
    else
      loop n (d + 1) factors
  in
    loop n 2 (List.init 0 id)

let rec count n =
  let rec loop n acc = 
    if n < 5 then
      acc + 0
    else if n == 5 then
      acc + 1
    else
      loop (n - 1) (acc + List.length (List.filter (fun p -> p == 5) (factorize n)))
  in loop n 0

let main =
  let n = Scanf.scanf "%d\n" id in
  Printf.printf "%d\n" (count n)
