/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package spellchecker;

import java.util.List;
import org.languagetool.JLanguageTool;
import javax.xml.parsers.*;
import org.xml.sax.InputSource;
import org.w3c.dom.*;
import java.io.*;
import org.languagetool.language.Polish;
import org.languagetool.rules.RuleMatch;

/**
 *
 * @author zireael
 */
public class Spellchecker {

    /**
     * @param args the command line arguments
     */
    private static void wypiszWynikiDoPliku(String file, String wyjscie) {
        try {
            PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter(file, true)));
            out.println(wyjscie);
            out.close();
        } catch (IOException e) {
        }


    }

    public static void parserXML(String inputFile) {

        String result = "";
        try {

            int mistakes = 0;
            JLanguageTool langTool = new JLanguageTool(new Polish());
            langTool.activateDefaultPatternRules();
            DocumentBuilderFactory dbf =
                    DocumentBuilderFactory.newInstance();
            DocumentBuilder db = dbf.newDocumentBuilder();
            //      Document doc = db.parse(new FileInputStream(new File("retroc-dev-cleaned-500w.xml")));
            InputSource is = new InputSource();
            is.setCharacterStream(new StringReader(inputFile));

            Document doc = db.parse(is);
            NodeList nodes = doc.getElementsByTagName("portion");
            for (int i = 0; i < nodes.getLength(); i++) {
                Element element = (Element) nodes.item(i);
                String id = element.getAttribute("id");
                NodeList date = element.getElementsByTagName("date");
                Element line = (Element) date.item(0);
                String annee = line.getAttribute("annee");

                NodeList title = element.getElementsByTagName("texte");
                line = (Element) title.item(0);
                NodeList textChildren = line.getChildNodes();
                //  System.out.println(textChildren.getLength());
                String texte = "";
                for (int j = 0; j < textChildren.getLength(); j++) {
                    String child = textChildren.item(j).getNodeValue();
                    if (child != null) {
                        texte = texte + child;
                    }
                }
                List<RuleMatch> matches = langTool.check(texte);
                mistakes = 0;
                for (RuleMatch match : matches) {
                    mistakes++;
                }

                result = id + "    " + annee + "  " + mistakes;
                System.out.println(result);

            }
        } catch (Exception e) {
            e.printStackTrace();
        }



        //  return result;
    }

    public static void main(String[] args) throws IOException {
        String everything = "";
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer contents = new StringBuffer();
        String text = null;

        // repeat until all lines is read
        while ((text = br.readLine()) != null) {
            contents.append(text).append(System.getProperty("line.separator"));
        }
        br.close();


        everything = contents.toString();

        parserXML(everything);
    }
}
