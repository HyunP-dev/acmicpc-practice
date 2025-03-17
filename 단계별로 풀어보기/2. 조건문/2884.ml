type time = { hours: int; minutes: int }

let to_time h m = { hours = h; minutes = m }

let before t = 
  if t.minutes - 45 >= 0 then
    to_time t.hours (t.minutes - 45)
  else
    if t.hours - 1 >= 0 then
      to_time (t.hours - 1) (t.minutes + 60 - 45)
    else
      to_time (t.hours - 1 + 24) (t.minutes + 60 - 45)

let print_time t =
  print_int t.hours;
  print_string " ";
  print_int t.minutes

let _ = Scanf.scanf "%d %d" to_time
 |> before 
 |> print_time;
