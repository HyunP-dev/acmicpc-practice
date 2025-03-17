let price a b c = 
  (* 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다. *)
  if a = b && b = c then
    10000 + b * 1000
  else 
    (* 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다. *)
    if a = b || b = c then
      1000 + b * 100
    else
      if a == c then
        1000 + a * 100
      (* 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다. *)
      else
        100 * List.fold_left max min_int [a; b; c] 

let _ = Scanf.scanf "%d %d %d\n" price
 |> print_int
