/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package RecorridoArbol;

/**
 *
 * @author User
 */
public class Arbol {
    Nodo Raiz;
    
    Arbol(){
        Raiz = null;
    }
    
    public void insertar (int x){
        if (Raiz == null){
            Raiz = new Nodo(x);
            return;
        }
        Nodo p,q=null;
        p=Raiz;
        while(p!=null){
            if(x<p.info){
                q=p;
                p=p.izq;
            }else{
                if (x>p.info){
                    q=p;
                    p=p.dere;
                }else{
                    return;
                }
                
            }
        }
        if(x<q.info){
            q.izq = new Nodo(x);            
        }else{
            q.dere= new Nodo(x);
        }
    }
    
    void inorden (Nodo p) {
     
        if(p != null) {
            inorden(p.izq);
            System.out.println (p.info);
            inorden(p.dere);
        }     
    }
    
     void Preorden (Nodo p) {
     
        if(p != null) {
            System.out.println (p.info);
            inorden(p.izq);
            inorden(p.dere);
        }     
    }
    
     void Posorden (Nodo p) {
     
        if(p != null) {
            
            inorden(p.izq);
            inorden(p.dere);
            System.out.println (p.info);
        }     
    }
    
    
    
    
}
