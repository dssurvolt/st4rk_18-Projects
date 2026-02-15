import Data.Maybe (fromJust)

data SExpr
    = Integers Int
    | Symbols String
    | Lists [SExpr]
    deriving Show

data Ast 
    = Define { varName :: String
             , varValue :: Ast }
    | Call { funcName :: String
           , args :: [Ast] }
    | AstInteger Int
    | AstBool Bo
    | AstSymbol Stringol
    | AstList [Ast]
    | AstNil
    deriving (Show, Eq)

getSymbol :: SExpr -> Maybe String
getSymbol (Symbols s) = Just s
getSymbol _ = Nothing

getInteger :: SExpr -> Maybe Int
getInteger (Integers i) = Just i
getInteger _ = Nothing

getInteger1 :: Ast -> Maybe Int
getInteger1 (AstInteger i) = Just i
getInteger1 _ = Nothing

getList :: SExpr -> Maybe [SExpr]
getList (Lists xs) = Just xs
getList _ = Nothing

-- printTree :: SExpr -> Maybe String
-- printTree (Integers i) = Just "a Number" ++ (show i)
-- printTree (Symbols s) = Just "a Symbol" ++ (show s)
-- printTree (Lists x:xs) = Just "a List with" ++ printTree x ++ printTree (Lists xs)  

printTree :: SExpr -> String
printTree (Integers i) = "a Number " ++ show i
printTree (Symbols s) = "a Symbol " ++ s
printTree (Lists [])  = "a List with"
printTree (Lists (x:xs)) =
  "a List with " ++ describeElemInList x ++ describeRest xs

describeElemInList :: SExpr -> String
describeElemInList (Symbols s)  = "a Symbol '" ++ s ++ "'"
describeElemInList (Integers i) = "a Number " ++ show i
describeElemInList l@(Lists _)  = "(" ++ printTree l ++ ")"

describeRest :: [SExpr] -> String
describeRest []     = ""
describeRest [y]    = " followed by " ++ describeElemInList y
describeRest (y:ys) = " followed by " ++ describeElemInList y ++ describeTail ys

describeTail :: [SExpr] -> String
describeTail []     = ""
describeTail (z:zs) = " , " ++ describeElemInList z ++ describeTail zs

-- sexprToAST :: SExpr -> Maybe Ast
-- sexprToAST (Integers i) = Just (AstInteger i)
-- sexprToAST (Symbols s) = Just (AstSymbol s)
-- sexprToAST (Lists []) = Just (AstNil)
-- sexprToAST (Lists (x:xs)) = case sexprToAST x of
--     Just x' -> case sexprToAST (Lists xs) of
--         Just xs' -> Just (AstList (x':xs'))
--         Nothing -> Nothing
--     Nothing -> Nothing
-- sexprToAST (Lists _) = Nothing -- TODO: handle lists

sexprToAST :: SExpr -> Maybe Ast
sexprToAST (Integers i) = Just (AstInteger i)
sexprToAST (Symbols s) = Just (AstSymbol s)
sexprToAST (Lists []) = Just AstNil
sexprToAST (Lists xs) = case xs of
    [Symbols "define", Symbols name, value] -> do
        astValue <- sexprToAST value
        return $ Define name astValue
    [Symbols _, Symbols funcName, args] -> do
        astArgs <- mapM sexprToAST [args]
        return $ Call funcName astArgs
    _ -> Nothing
sexprToAST _ = Nothing



add :: Int -> Int -> Int
add x y = x + y

main :: IO()
main = putStrLn (show (add 2 3))