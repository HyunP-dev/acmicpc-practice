let rec is_palindrome s =
  match s with
  | _ when String.length s < 2 -> true
  | _ ->
    is_palindrome (String.sub s 1 (String.length s - 2))
    && s.[0] == s.[String.length s - 1]
;;

let rec main () =
  match read_line () with
  | "0" -> exit 0
  | s ->
    print_endline (if is_palindrome s then "yes" else "no");
    main ()
;;

let () = main ()
