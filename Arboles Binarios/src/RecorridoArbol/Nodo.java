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
public class Nodo {
    int  info;
    Nodo izq;
    Nodo dere;
    Nodo (int info){
        this.info=info;
        izq = null;
        dere = null;
    }
}
