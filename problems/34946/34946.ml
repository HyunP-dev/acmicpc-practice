let id = fun a b c d -> a, b, c, d

let main =
  let a, b, c, d = Scanf.scanf "%d %d %d %d\n" id in
  let shuttle = a + b <= d in
  let walk = c <= d in
  let result =
    if shuttle && walk
    then "~.~"
    else if shuttle
    then "Shuttle"
    else if walk
    then "Walk"
    else "T.T"
  in
  print_endline result
;;
