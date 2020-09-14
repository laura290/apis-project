import sys
import argparse
import pandas as pd
import funciones as fn

def parse():
    
    parser = argparse.ArgumentParser(description = "Accede a informión sobre los partidos de los distintos paises")
    parser.add_argument("-d" ,dest="date",type=int,help="Escribe el año del partido (Entre comillas 'date')", default=None)
    parser.add_argument("-t" ,dest="tournament",type=str,help="Escribe el tipo de torneo",default=None)
    parser.add_argument("-c" ,dest="country",type=str,help="Introduce el país que deseas", default=None)
    parser.add_argument("-f" ,dest="fifa_code",type=str,help="Introduce el codigo de pais fifa que desea:\n - Euro\n - AFC Championship\n - Tournoi de France\n -SheBelieves Cup\n)",default=None)
     
    args = parser.parse_args()
    return(args)

def main():
    args = parse()
    date = args.date
    fifa_code = args.fifa_code
    tournament= args.tournament
    country = args.country
    fn.seleccion_pais(args.country)
    if args.country !=None:
        print(fn.seleccion_pais(country))
        
   
if __name__=="__main__":
    main()