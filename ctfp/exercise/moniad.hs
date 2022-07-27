class MyMonoid m where
    mempty :: m
    mappend :: m -> m -> m

instance MyMonoid String where
    mempty = ""
    mappend = (++)

main = putStrLn "Hello"++"Haskell!"