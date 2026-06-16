import javax.swing.*;
import java.awt.*;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class Prac4 extends JFrame implements KeyListener {
    private JLabel displayLabel;
    private StringBuilder displayText;
    private static final int MAX_LENGTH = 6;

    public Prac4() {
        setTitle("7-Segment LCD Display");
        setSize(400, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        displayText = new StringBuilder(" ".repeat(MAX_LENGTH));
        displayLabel = new JLabel(displayText.toString(), SwingConstants.CENTER);
        displayLabel.setFont(new Font("Digital-7", Font.BOLD, 40));
        displayLabel.setOpaque(true);
        displayLabel.setBackground(Color.BLACK);
        displayLabel.setForeground(Color.GREEN);

        add(displayLabel, BorderLayout.CENTER);
        addKeyListener(this);
        setFocusable(true);
    }

    private void updateDisplay(char newChar) {
        displayText.deleteCharAt(0);
        displayText.append(newChar);
        displayLabel.setText(displayText.toString());
    }

    @Override
    public void keyTyped(KeyEvent e) {
        updateDisplay(e.getKeyChar());
    }

    @Override
    public void keyPressed(KeyEvent e) {}

    @Override
    public void keyReleased(KeyEvent e) {}

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Prac4 lcd = new Prac4();
            lcd.setVisible(true);
        });
    }
}
