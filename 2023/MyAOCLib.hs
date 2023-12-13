module MyAOCLib where

readLines :: FilePath -> IO [String]
readLines = fmap lines . readFile

splitRaw :: (Eq a) => [a] -> a -> [a] -> [[a]]
splitRaw [] c partialWord = [partialWord]
splitRaw (x:s) c partialWord
    | x == c    = [partialWord] ++ splitRaw s c []
    | otherwise = splitRaw s c (partialWord ++ [x])

split :: (Eq a) => a -> [a] -> [[a]]
split c s = splitRaw s c []

lstrip :: Char -> String -> String
lstrip c (x:s)
    | c == x    = lstrip c s
    | otherwise = x:s

-- TODO: Use `Maybe`
getFirstIndex :: (Eq a) => a -> [a] -> Int
getFirstIndex _ [] = error "No occurence"
getFirstIndex y (x:xs)
    | x == y    = 0
    | otherwise = 1 + getFirstIndex y xs


getIndices :: (Eq a) => a -> [a] -> [Int]
getIndices = getIndices' 0
    where
        getIndices' :: (Eq a) => Int -> a -> [a] -> [Int]
        getIndices' _ _ [] = []
        getIndices' index symbol (x:xs)
            | x == symbol   = index:rest
            | otherwise     = rest
            where rest = getIndices' (index+1) symbol xs

quickSort :: (Ord a) => [a] -> [a]
quickSort [] = []
quickSort (x:xs) = smallerSorted ++ (x:largerSorted)
    where
        smallerSorted = quickSort $ filter (<=x) xs
        largerSorted = quickSort $ filter (>x) xs

transpose :: [[a]] -> [[a]]
transpose [] = []
transpose matrix
    | (length $ head matrix) == 1   = [[x | [x] <- matrix]]
    | otherwise = (map head matrix):(transpose $ map tail matrix)

