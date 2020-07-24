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
public class Main {
    
    public static void main(String [] args ){
        Arbol arbol = new Arbol();
        arbol.insertar(10);
        arbol.insertar(8);
        arbol.insertar(20);
        arbol.insertar(13);
        arbol.insertar(12);
        arbol.insertar(9);
        arbol.insertar(4);
        arbol.insertar(2);
        arbol.insertar(7);
        arbol.inorden(arbol.Raiz);
        System.out.println("------------");
        arbol.Preorden(arbol.Raiz);
        System.out.println("------------");
        arbol.Posorden(arbol.Raiz);
        
        
        
    }
    
    
    
}
