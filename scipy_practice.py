# scipy_practice.py

# ****************************************
# 1) SOLVE LINEAR SYSTEM Ax = b
# ****************************************
from scipy.linalg import solve
A = [[3, 2], [1, -1]]
b = [5, 1]
solution = solve(A, b)
print("Solution [x, y]:", solution)





# ****************************************
# 2) MINIMIZE A SCALAR FUNCTION 
# ****************************************
from scipy.optimize import minimize

def scalar_f(t): return (t - 3)**2 + np.sin(t)

# default method is BFGS
model = minimize(scalar_f, x0=0)
opt = model.x[0]
print("Minimizer t* =", opt)
print("Minimum f(t*) =", scalar_f(opt))





# ****************************************
# 2) EIGENVALUE DECOMPOSITION AND SVD
# ****************************************
from scipy.linalg import eig, svd
# eigenvalue decomposition
M1= [[4,2], [1,3]]
eigenvalues, eigenvectors = eig(M1)

# singular value decomposition
M2 = np.array([[1, 2, 3], [4, 5, 6]])
print(f"M2 shape: {M.shape}")

# compute full SVD, returns: U in (2x2), s in (2x1), V in (3x3)
U, s, V = svd(M2)

# check that U and V are orthogonal
assert np.allclose(np.all(U.T @ U == np.eye(U.shape[0]))), "U is not orthogonal!"
assert np.allclose(np.all(V.T @ V == np.eye(V.shape[0]))), "V is not orthogonal!"

# build full `Sigma` of shape (2×3) from vector `s`
Sigma = np.zeros((U.shape[0],V.shape[0]))
# place s[0], s[1] on diagonal
Sigma[np.diag_indices(len(s))] = s

# reconstruct `M2`
M2_reconstructed = U @ Sigma @ Vh
# check that `M2_reconstructed` is close to `M2` (within floating-point tolerance)
assert np.allclose(M2, M2_reconstructed)


