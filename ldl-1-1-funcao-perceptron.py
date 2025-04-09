# primeiro elemento no vetor x deve ser 1
# tamanho de w e x deve ser n+1 para neuronios com n entradas
def compute_output(w,x) :
    z = 0.0
    for i in range(len(w)) :
        z = z + x[i] * w[i] # computa a soma dos pesos
    if z < 0 : # aplica a funcao sinal
        return -1
    else :
        return 1
    
print (compute_output([0.9,-0.6,-0.5],[1.0,-1.0,-1.0]))
print (compute_output([0.9,-0.6,-0.5],[1.0,-1.0,1.0]))
print (compute_output([0.9,-0.6,-0.5],[1.0,1.0,-1.0]))
print (compute_output([0.9,-0.6,-0.5],[1.0,1.0,1.0]))
