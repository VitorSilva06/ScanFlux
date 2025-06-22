import cv2
from pyzbar.pyzbar import decode
import numpy as np
import os

class Leitor:
    def ler_codigo_barras_camera(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Erro ao abrir a câmera")
            return None

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            codigos = decode(frame)
            for codigo in codigos:
                dados_lidos = codigo.data.decode('utf-8')
                pts = [(pt.x, pt.y) for pt in codigo.polygon]
                cv2.polylines(frame, [np.array(pts, np.int32)], True, (0, 255, 0), 2)
                cv2.putText(frame, dados_lidos, (pts[0][0], pts[0][1]-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                cv2.imshow("Etiqueta", frame)
                cv2.waitKey(1000)
                cap.release()
                cv2.destroyAllWindows()
                return dados_lidos

            cv2.imshow("Escaneie a etiqueta", frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break

        cap.release()
        cv2.destroyAllWindows()
        return None

    def ler_codigo_barras_imagem(self, caminho_imagem):
        imagem = cv2.imread(caminho_imagem)
        if imagem is None:
            print("Erro ao carregar a imagem. Verifique o caminho.")
            return []

        codigos = decode(imagem)
        resultados = []

        for codigo in codigos:
            dados = codigo.data.decode('utf-8')
            tipo = codigo.type
            print(f"Dados: {dados}")
            resultados.append((tipo, dados))

            pts = [(pt.x, pt.y) for pt in codigo.polygon]
            cv2.polylines(imagem, [np.array(pts, dtype=np.int32)], True, (0, 255, 0), 2)
            cv2.putText(imagem, dados, (pts[0][0], pts[0][1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # Mostra a imagem com os códigos destacados
        cv2.imshow("Resultado da Imagem", imagem)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return resultados
