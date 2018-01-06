DIR="/home/fmora/workspace/freud-tool/examples"
FOLDER=$1
EXAMPLE=$2

freud ${DIR}/${FOLDER}/${EXAMPLE}/${EXAMPLE}.py ${DIR}/${FOLDER}/${EXAMPLE}/${EXAMPLE}_1.py --client ${EXAMPLE} --library lib int [int,int]