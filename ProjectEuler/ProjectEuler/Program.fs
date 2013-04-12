// Learn more about F# at http://fsharp.net
// See the 'F# Tutorial' project for more help.
open System
open System.Collections.Generic

let SieveOfEratosthenes limit =
    let filtered = new Dictionary<int, bool>();
    for n in [1..limit] do filtered.Add(n, false);

    for n in [2..limit] do
        if filtered.[n] = false then
            for x in [n+n..n..limit] do filtered.[x] <- true

    [for entry in filtered do if entry.Value = false then yield entry.Key]

let distrib e L =
    let rec aux pre post = 
        seq {
            match post with
            | [] -> yield (L @ [e])
            | h::t -> yield (List.rev pre @ [e] @ post)
                      yield! aux (h::pre) t 
        }
    aux [] L

let rec perms = function 
    | [] -> Seq.singleton []
    | h::t -> Seq.collect (distrib h) (perms t)

let PermuteInteger (n: int) =
    let permutations = perms [for char in n.ToString() -> char]
    [for p in permutations do
        let sb = new System.Text.StringBuilder(p.Length)
        p |> List.iter (fun c -> sb.Append(c) |> ignore)
        yield Convert.ToInt32(sb.ToString())]

let CumulativeList (input: int list) =
    let rec iterate (input: int list, output: int list) = 
        match input with
        | a::[] -> output @ [a]
        | a::b -> iterate (b, output @ [a])
        | [] -> []
    iterate (input, [])

let Problem49() =
    // The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, 
    // is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 
    // 4-digit numbers are permutations of one another.
    //
    // There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting 
    //this property, but there is one other 4-digit increasing sequence.
    //What 12-digit number do you form by concatenating the three terms in this sequence?
    let primes = SieveOfEratosthenes 9999 |> List.filter (fun x -> x > 999) |> Set.ofList
    let answers = [for prime in primes do
                       let permutations = PermuteInteger prime |> Set.ofList
                       let primePermutations = Set.intersect primes permutations
                       if primePermutations.Count >= 3 then
                           for a in primePermutations do
                               for b in primePermutations do
                                   for c in primePermutations do
                                       if a <> b && a <> c && b <> c then
                                           let sorted = [a; b; c] |> List.sort
                                           if (b - a) = (c - b) then yield sorted]
    let answerStrings = answers |> List.map (fun x ->
                                                let sb = System.Text.StringBuilder(12);
                                                x |> List.iter (fun c -> sb.Append(c) |> ignore)
                                                sb.ToString())
                                |> Set.ofList |> (fun x -> x - (["148748178147"] |> Set.ofList)) |> Set.toList                   
    answerStrings.Head

let Problem50() = 
    // The prime 41, can be written as the sum of six consecutive primes:
    // 41 = 2 + 3 + 5 + 7 + 11 + 13
    // This is the longest sum of consecutive primes that adds to a prime below one-hundred.
    // The longest sum of consecutive primes below one-thousand that adds to a prime, contains 
    // 21 terms, and is equal to 953.
    // Which prime, below one-million, can be written as the sum of the most consecutive primes?
    let primes = SieveOfEratosthenes 1000000 
    let summed = CumulativeList primes
    0
                

[<EntryPoint>]
let main argv = 
    let answer = Problem50()
    0 // return an integer exit code
