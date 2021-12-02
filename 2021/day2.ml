let input = open_in "day2.in" in

(* imperative solutions *)
let solA input =
  let depth = ref 0 in
  let horizontal = ref 0 in
  let over = ref false in
  while not !over do
    let line = try input_line input with
    | End_of_file -> (over := true); "" in
    if not !over then (
      let words = String.split_on_char ' ' line in
      let num = int_of_string (List.nth words 1) in
      match (List.hd words) with
      | "forward" -> (horizontal := !horizontal + num)
      | "up" -> (depth := !depth - num)
      | "down" -> (depth := !depth + num)
      | _ -> ()
    )
  done;
  print_int (!depth * !horizontal);
  print_newline ();
in

let solB input =
  let depth = ref 0 in
  let horizontal = ref 0 in
  let aim = ref 0 in
  let over = ref false in
  while not !over do
    let line = try input_line input with
    | End_of_file -> (over := true); "" in
    if not !over then (
      let words = String.split_on_char ' ' line in
      let num = int_of_string (List.nth words 1) in
      match (List.hd words) with
      | "forward" -> (horizontal := !horizontal + num; depth := !depth + !aim * num)
      | "up" -> (aim := !aim - num)
      | "down" -> (aim := !aim + num)
      | _ -> ()
    )
  done;
  print_int (!depth * !horizontal);
  print_newline ();
in

(* More functional solutions *)
let read_lines input = 
  let l = ref [] in
  let over = ref false in
  while not !over do
    let line = try input_line input with
    | End_of_file -> (over := true); "" in
    if not !over then l := line :: !l
  done;
  List.rev !l
in

let solA_2 input =
  let lines = read_lines input in
  let init = (0, 0) in
  let res = List.fold_left (fun state -> fun next ->
    let (depth, horiz) = state in
    match (String.split_on_char ' ' next) with
    | "forward" :: x :: [] -> (depth, horiz + int_of_string x)
    | "up" :: x :: [] -> (depth - int_of_string x, horiz)
    | "down" :: x :: [] -> (depth + int_of_string x, horiz)
    | _ -> raise (Failure "parse error")
  ) init lines in
  print_int (fst res * snd res);
  print_newline ();
in

let solB_2 input =
  let lines = read_lines input in
  let init = (0, 0, 0) in
  let res = List.fold_left (fun state -> fun next ->
    let (depth, horiz, aim) = state in
    match (String.split_on_char ' ' next) with
    | "forward" :: x :: [] -> (depth + (aim * int_of_string x), horiz + int_of_string x, aim)
    | "up" :: x :: [] -> (depth, horiz, aim - int_of_string x)
    | "down" :: x :: [] -> (depth, horiz, aim + int_of_string x)
    | _ -> raise (Failure "parse error")
  ) init lines in
  let (depth, horiz, aim) = res in
  print_int (depth * horiz);
  print_newline ();
in

solB_2 input
