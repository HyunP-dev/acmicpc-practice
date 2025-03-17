type time = { hours: int; minutes: int }

let to_time h m = { hours = h; minutes = m }

let from_minutes m = { hours = m / 60; minutes = m mod 60 }

let after_minutes m t = 
  if t.minutes + m >= 60 then
    if t.hours + 1 >= 24 then
      to_time ((t.hours + 1) mod 24) ((t.minutes + m) mod 60)
    else
      to_time (t.hours + 1) ((t.minutes + m) mod 60)
  else
    to_time t.hours (t.minutes + m)

let after_hours h t =
  if t.hours + h >= 24 then
    to_time ((t.hours + h) mod 24) t.minutes
  else
    to_time (t.hours + h) t.minutes

let after dt t = t
 |> after_minutes dt.minutes
 |> after_hours dt.hours

let print_time t =
  print_int t.hours;
  print_string " ";
  print_int t.minutes

let _ = Scanf.scanf "%d %d\n" to_time
 |> after (Scanf.scanf "%d" from_minutes)
 |> print_time;
