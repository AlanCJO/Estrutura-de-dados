<?php 

class VetorNaoOrdenado
{
    public function __construct(int $capacidade)
    {
        $this->capacidade = $capacidade;
        $this->ultima_posicao = -1;
        $this->valores = array();
    }

    # O(n)
    public function imprime()
    {
        if($this->capacidade === -1) {
            echo "O vetor está vazio!";
        } else {
            for($i = 0; $i <= $this->ultima_posicao; $i++) 
            {
                echo "\n{$i} - {$this->valores[$i]}";
            }
        }
    }

    # O(1) - O(2)
    public function insere($valor) 
    {
        if ($this->ultima_posicao === $this->capacidade - 1) {
            echo "Capacidade máxima atingida!";
        } else {
            $this->ultima_posicao++;
            $this->valores[$this->ultima_posicao] = $valor;
        }
    }

    # O(n)
    public function pesquisar($valor)
    {
        $ultima_posicao = $this->ultima_posicao;
        echo "\n---------------------";
        $i = 0;
        while($i < $ultima_posicao + 1)
        {
            echo "\n"; 
            echo $i;
            if ($valor == $this->valores[$i]);
                return $i;
            $i++;
        }
        echo "\n---------------------";


        // for ($i = 0; $i < $ultima_posicao + 1; $i++)
        // {
        //     echo "\n"; 
        //     echo $i;
        //     if ($valor == $this->valores[$i]);
        //         return $i;
        // }
        // echo "\n---------------------";

        
        return null;
    }

    # O(n)
    public function excluir($valor)
    {
        $posicao = $this->pesquisar($valor);
        if (!isset($posicao)) {
        } else {
            for ($i = $posicao; $i < $this->ultima_posicao; $i++)
            {
                $this->valores[$i] = $this->valores[$i + 1];
            }
            $this->ultima_posicao--;
        }
    }
}


$vetor = new VetorNaoOrdenado(5);
$vetor->insere(3);
$vetor->insere(2);
$vetor->insere(1);

echo "\n";
$vetor->imprime();

echo "\n";
echo "\n".$vetor->pesquisar(3);
echo "\n".$vetor->pesquisar(0);

$vetor->excluir(2);

echo "\n";
$vetor->imprime();


$vetor->insere(4);
$vetor->insere(5);

echo "\n";
$vetor->imprime();

echo "\n\n";


?>