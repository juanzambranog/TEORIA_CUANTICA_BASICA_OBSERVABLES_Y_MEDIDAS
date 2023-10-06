import numpy as np
def transicion(v1,v2):

    norma_v1=np.linalg.norm(v1)
    for i in range(len(v1)):
        v1[i]=v1[i]/norma_v1
        return v1
    norma_v2= np.linalg.norm(v2)
    for i in range(len(v2)):
        v2[i] = v2[i] / norma_v2
        return v2


    for i in range(len(v1)):
        v1[i] = v1[i].conjugate()
        interno=np.inner(v1,v2)
    return interno

print(transicion([1,2,3],[4,5,6]))

def hermitiana_media_varianza(m,v):
    def b(v):
        for i in range(len(v)):
            v[i] = v[i].conjugate()
        return v

    def accion(v, m):
        ans = [0] * len(m)
        for i in range(len(m)):
            aux = 0
            for j in range(len(m[i])):
                aux += m[i][j] * v[j]
            ans[i] = aux
        return ans

    def prod_inter(v1, v2):
        ans = 0
        for i in range(len(v1)):
            v1[i] = v1[i].conjugate()
            ans += v1[i] * v2[i]
        return ans

    def prod_mat(m1, m2):
        ans = [[0 for j in range(len(m2[0]))] for i in range(len(m1))]
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                aux = 0
                for k in range(len(m2)):
                    aux = m1[i][k] * m2[k][j]
                ans[i][j] = aux
        return ans
    b_v=b(v)
    ax_v=accion(v,m)
    media=prod_inter(ax_v,b_v)
    matri=[[media * -1 for i in range(len(m[0]))] for j in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m)):
            matri[i][j] += m[i][j]
    matriz=prod_mat(matri,matri)
    var=prod_inter(accion(v,matriz),b_v)
    return media,var