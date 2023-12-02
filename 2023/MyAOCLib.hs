module MyAOCLib where

readLines :: FilePath -> IO [String]
readLines = fmap lines . readFile

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
