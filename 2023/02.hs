module Main
    where

import Data.Map (Map)
import qualified Data.Map as Map
import Data.Maybe (fromJust, isJust)

splitRaw :: String -> Char -> String -> [String]
splitRaw "" c partialWord = [partialWord]
splitRaw (x:s) c partialWord
    | x == c    = [partialWord] ++ splitRaw s c ""
    | otherwise = splitRaw s c (partialWord ++ [x])

split :: Char -> String -> [String]
split c s = splitRaw s c ""

lstrip :: Char -> String -> String
lstrip c (x:s)
    | c == x    = lstrip c s
    | otherwise = x:s

---

getColoredMarbles :: Char -> [[String]] -> Int
getColoredMarbles color throws =
    let colorMissing = null [throw | throw <- throws, (throw!!1)!!0 == color]
    in if colorMissing
        then 0
        else read ([throw!!0 | throw <- throws, (throw!!1)!!0 == color]!!0)

rawToGame :: String -> [Int]
rawToGame s = [r, g, b]
    where   r = getColoredMarbles 'r' throws
            g = getColoredMarbles 'g' throws
            b = getColoredMarbles 'b' throws
            throws = [split ' ' (lstrip ' ' x) | x <- (split ',' s)]

rawToGames :: String -> [[Int]]
rawToGames s = map rawToGame [lstrip ' ' x | x <- (split ';' s)]

readLines :: FilePath -> IO [String]
readLines = fmap lines . readFile

validateDraw :: [Int] -> [Int] -> Bool
validateDraw x x0 = all (==True) [a <= a0 | (a, a0) <- zip x x0]

validateGame :: [[Int]] -> [Int] -> Bool
validateGame l rules = all (==True) [validateDraw x rules | x <- l]

validateRawGame :: String -> [Int] -> Bool
validateRawGame rawGame rules = validateGame game rules
    where game = rawToGames (tail ((split ':' rawGame)!!1))

gameId :: String -> Int
gameId s = read idString
    where   gameString = (split ':' s)!!0
            idString = (split ' ' gameString)!!1

part1 :: [String] -> Int
part1 l = sum [gameId line | line <- l, validateRawGame line [12,13,14]]

main = do
    rawInput <- (readLines "02.in")
    putStrLn (show (part1 rawInput))
