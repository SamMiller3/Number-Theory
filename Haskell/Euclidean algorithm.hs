euclidean :: Integral a => a -> a -> a
euclidean x 0 = x
euclidean x y = euclidean y (x `mod` y) 
