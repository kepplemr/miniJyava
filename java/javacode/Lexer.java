/* The following code was generated by JFlex 1.4_pre3 on 12/3/13 9:17 PM */

package javacode;
import java_cup.runtime.*;


/**
 * This class is a scanner generated by 
 * <a href="http://www.jflex.de/">JFlex</a> 1.4_pre3
 * on 12/3/13 9:17 PM from the specification file
 * <tt>file:/home/michael/workspace/MiniJyava/flex/Scanner.jflex</tt>
 */
class Lexer implements java_cup.runtime.Scanner, sym {

  /** This character denotes the end of file */
  public static final int YYEOF = -1;

  /** initial size of the lookahead buffer */
  private static final int YY_BUFFERSIZE = 16384;

  /** lexical states */
  public static final int STRING = 1;
  public static final int YYINITIAL = 0;

  /** 
   * Translates characters to character classes
   */
  private static final char [] yycmap = {
     7,  7,  7,  7,  7,  7,  7,  7,  7,  3,  2,  0,  3,  1,  7,  7, 
     7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  0,  0,  0,  0, 
     3, 43,  5,  0,  6,  0, 49, 51, 35, 36,  9, 44, 42, 45, 34,  8, 
     4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  0, 41, 47, 48, 46,  0, 
     0,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6, 
     6,  6,  6, 31,  6,  6,  6,  6,  6,  6,  6, 39, 10, 40,  0,  6, 
     0, 17, 11, 22, 23, 12, 26, 13, 27, 14,  6,  6, 21, 33, 15, 20, 
    30,  6, 18, 19, 25, 29, 16, 28, 24, 32,  6, 37, 50, 38,  0,  7
  };


  /** 
   * Translates a state to a row index in the transition table (packed version)
   */
  final private static String yy_rowMap_packed = 
    "\0\0\0\64\0\150\0\234\0\320\0\u0104\0\u0138\0\320\0\u016c\0\u01a0"+
    "\0\u01d4\0\u0208\0\u023c\0\u0270\0\u02a4\0\u02d8\0\u030c\0\u0340\0\u0374\0\u03a8"+
    "\0\u03dc\0\u0410\0\320\0\320\0\320\0\320\0\320\0\320\0\320\0\320"+
    "\0\320\0\u0444\0\320\0\320\0\u0478\0\u04ac\0\u04e0\0\u0514\0\u0548\0\u057c"+
    "\0\u05b0\0\320\0\320\0\u05e4\0\u0618\0\u064c\0\u0680\0\u06b4\0\u06e8\0\u071c"+
    "\0\u0750\0\u0784\0\u0104\0\u07b8\0\u07ec\0\u0820\0\u0854\0\u0888\0\u08bc\0\u08f0"+
    "\0\u0924\0\u0958\0\u098c\0\u09c0\0\u09f4\0\u0a28\0\u0a5c\0\320\0\320\0\320"+
    "\0\320\0\320\0\320\0\320\0\320\0\320\0\320\0\320\0\320\0\320"+
    "\0\320\0\320\0\u0618\0\320\0\u0a90\0\u0ac4\0\u0af8\0\u0b2c\0\u0b60\0\u0b94"+
    "\0\u0104\0\u0104\0\u0bc8\0\u0bfc\0\u0c30\0\u0c64\0\u0c98\0\u0ccc\0\u0d00\0\u0d34"+
    "\0\u0d68\0\u0d9c\0\u0dd0\0\u0e04\0\u0e38\0\u0e6c\0\u0ea0\0\u0ed4\0\u0f08\0\u0104"+
    "\0\u0f3c\0\u0104\0\u0104\0\u0f70\0\u0fa4\0\u0fd8\0\u100c\0\u0104\0\u0104\0\u1040"+
    "\0\u1074\0\u10a8\0\u10dc\0\u1110\0\u1144\0\u1178\0\u11ac\0\u11e0\0\u1214\0\u1248"+
    "\0\u127c\0\u0104\0\u0104\0\u0104\0\u12b0\0\u12e4\0\u1318\0\u134c\0\u1380\0\u13b4"+
    "\0\u13e8\0\u0104\0\u0104\0\u0104\0\u0104\0\u0104\0\u141c\0\u1450\0\u0104\0\u0104"+
    "\0\u0104\0\u1484\0\u14b8\0\u14ec\0\u0104\0\u1520\0\u1554\0\u1588\0\u15bc\0\u15f0"+
    "\0\u1624\0\u1658\0\u168c\0\u16c0\0\320";

  /** 
   * Translates a state to a row index in the transition table
   */
  final private static int [] yy_rowMap = yy_unpack_rowMap(yy_rowMap_packed);


  /** 
   * Unpacks the compressed row translation table.
   *
   * @param packed   the packed row translation table
   * @return         the unpacked row translation table
   */
  private static int [] yy_unpack_rowMap(String packed) {
    int [] map = new int[330];
    int i = 0;  /* index in packed string  */
    int j = 0;  /* index in unpacked array */
    while (i < 330) {
      int high = ((int) packed.charAt(i++)) << 16;
      map[j++] = high | packed.charAt(i++);
    }
    return map;
  }
  /** 
   * The packed transition table of the DFA (part 0)
   */
  private static final String yy_packed0 = 
    "\1\0\3\3\1\4\1\5\1\6\1\0\1\7\1\10"+
    "\1\0\1\11\1\12\1\6\1\13\1\14\1\15\1\6"+
    "\1\16\1\17\1\6\1\20\1\21\2\6\1\22\1\23"+
    "\1\6\1\24\1\6\1\25\1\26\2\6\1\27\1\30"+
    "\1\31\1\32\1\33\1\34\1\35\1\36\1\37\1\40"+
    "\1\41\1\42\1\43\1\44\1\45\1\46\1\47\1\0"+
    "\1\50\1\51\1\52\2\50\1\53\4\50\1\54\51\50"+
    "\1\0\3\3\64\0\1\4\147\0\1\6\1\0\2\6"+
    "\3\0\27\6\32\0\1\55\1\56\56\0\1\6\1\0"+
    "\2\6\3\0\1\6\1\57\7\6\1\60\15\6\26\0"+
    "\1\6\1\0\2\6\3\0\4\6\1\61\5\6\1\62"+
    "\2\6\1\63\11\6\26\0\1\6\1\0\2\6\3\0"+
    "\4\6\1\64\12\6\1\65\7\6\26\0\1\6\1\0"+
    "\2\6\3\0\1\6\1\66\20\6\1\67\4\6\26\0"+
    "\1\6\1\0\2\6\3\0\11\6\1\70\15\6\26\0"+
    "\1\6\1\0\2\6\3\0\1\6\1\71\25\6\26\0"+
    "\1\6\1\0\2\6\3\0\16\6\1\72\10\6\26\0"+
    "\1\6\1\0\2\6\3\0\1\6\1\73\25\6\26\0"+
    "\1\6\1\0\2\6\3\0\12\6\1\74\14\6\26\0"+
    "\1\6\1\0\2\6\3\0\7\6\1\75\10\6\1\76"+
    "\6\6\26\0\1\6\1\0\2\6\3\0\6\6\1\77"+
    "\20\6\26\0\1\6\1\0\2\6\3\0\20\6\1\100"+
    "\6\6\26\0\1\6\1\0\2\6\3\0\22\6\1\101"+
    "\4\6\26\0\1\6\1\0\2\6\3\0\16\6\1\102"+
    "\6\6\1\103\1\6\102\0\1\104\63\0\1\105\63\0"+
    "\1\106\63\0\1\107\64\0\1\110\64\0\1\111\1\0"+
    "\1\50\2\0\2\50\1\0\4\50\1\0\51\50\2\0"+
    "\1\52\61\0\2\112\1\0\2\112\1\113\4\112\1\114"+
    "\1\115\3\112\1\116\2\112\1\117\6\112\1\120\1\121"+
    "\30\112\1\122\1\55\1\123\1\124\61\55\11\125\1\0"+
    "\52\125\4\0\1\6\1\0\2\6\3\0\2\6\1\126"+
    "\24\6\26\0\1\6\1\0\2\6\3\0\11\6\1\127"+
    "\15\6\26\0\1\6\1\0\2\6\3\0\14\6\1\130"+
    "\12\6\26\0\1\6\1\0\2\6\3\0\10\6\1\131"+
    "\16\6\26\0\1\6\1\0\2\6\3\0\16\6\1\132"+
    "\10\6\26\0\1\6\1\0\2\6\3\0\16\6\1\133"+
    "\10\6\26\0\1\6\1\0\2\6\3\0\21\6\1\134"+
    "\5\6\26\0\1\6\1\0\2\6\3\0\12\6\1\135"+
    "\14\6\26\0\1\6\1\0\2\6\3\0\3\6\1\136"+
    "\23\6\26\0\1\6\1\0\2\6\3\0\16\6\1\137"+
    "\10\6\26\0\1\6\1\0\2\6\3\0\6\6\1\140"+
    "\20\6\26\0\1\6\1\0\2\6\3\0\4\6\1\141"+
    "\22\6\26\0\1\6\1\0\2\6\3\0\6\6\1\142"+
    "\20\6\26\0\1\6\1\0\2\6\3\0\22\6\1\143"+
    "\4\6\26\0\1\6\1\0\2\6\3\0\3\6\1\144"+
    "\23\6\26\0\1\6\1\0\2\6\3\0\12\6\1\145"+
    "\14\6\26\0\1\6\1\0\2\6\3\0\3\6\1\146"+
    "\23\6\26\0\1\6\1\0\2\6\3\0\1\147\26\6"+
    "\26\0\1\6\1\0\2\6\3\0\7\6\1\150\17\6"+
    "\26\0\1\6\1\0\2\6\3\0\10\6\1\151\16\6"+
    "\22\0\11\125\1\152\52\125\4\0\1\6\1\0\2\6"+
    "\3\0\3\6\1\153\23\6\26\0\1\6\1\0\2\6"+
    "\3\0\12\6\1\154\14\6\26\0\1\6\1\0\2\6"+
    "\3\0\5\6\1\155\21\6\26\0\1\6\1\0\2\6"+
    "\3\0\1\6\1\156\25\6\26\0\1\6\1\0\2\6"+
    "\3\0\1\6\1\157\25\6\26\0\1\6\1\0\2\6"+
    "\3\0\12\6\1\160\14\6\26\0\1\6\1\0\2\6"+
    "\3\0\14\6\1\161\12\6\26\0\1\6\1\0\2\6"+
    "\3\0\22\6\1\162\4\6\26\0\1\6\1\0\2\6"+
    "\3\0\16\6\1\163\10\6\26\0\1\6\1\0\2\6"+
    "\3\0\2\6\1\164\24\6\26\0\1\6\1\0\2\6"+
    "\3\0\10\6\1\165\16\6\26\0\1\6\1\0\2\6"+
    "\3\0\1\6\1\166\25\6\26\0\1\6\1\0\2\6"+
    "\3\0\10\6\1\167\16\6\26\0\1\6\1\0\2\6"+
    "\3\0\10\6\1\170\16\6\26\0\1\6\1\0\2\6"+
    "\3\0\12\6\1\171\14\6\26\0\1\6\1\0\2\6"+
    "\3\0\12\6\1\172\14\6\26\0\1\6\1\0\2\6"+
    "\3\0\3\6\1\173\23\6\26\0\1\6\1\0\2\6"+
    "\3\0\16\6\1\174\10\6\22\0\10\125\1\124\1\152"+
    "\52\125\4\0\1\6\1\0\2\6\3\0\4\6\1\175"+
    "\22\6\26\0\1\6\1\0\2\6\3\0\1\6\1\176"+
    "\25\6\26\0\1\6\1\0\2\6\3\0\6\6\1\177"+
    "\20\6\26\0\1\6\1\0\2\6\3\0\4\6\1\200"+
    "\22\6\26\0\1\6\1\0\2\6\3\0\7\6\1\201"+
    "\17\6\26\0\1\6\1\0\2\6\3\0\3\6\1\202"+
    "\23\6\26\0\1\6\1\0\2\6\3\0\16\6\1\203"+
    "\10\6\26\0\1\6\1\0\2\6\3\0\10\6\1\204"+
    "\16\6\26\0\1\6\1\0\2\6\3\0\1\6\1\205"+
    "\25\6\26\0\1\6\1\0\2\6\3\0\1\6\1\206"+
    "\25\6\26\0\1\6\1\0\2\6\3\0\3\6\1\207"+
    "\23\6\26\0\1\6\1\0\2\6\3\0\4\6\1\210"+
    "\22\6\26\0\1\6\1\0\2\6\3\0\1\6\1\211"+
    "\25\6\26\0\1\6\1\0\2\6\3\0\5\6\1\212"+
    "\21\6\26\0\1\6\1\0\2\6\3\0\6\6\1\213"+
    "\20\6\26\0\1\6\1\0\2\6\3\0\7\6\1\214"+
    "\17\6\26\0\1\6\1\0\2\6\3\0\14\6\1\215"+
    "\12\6\26\0\1\6\1\0\2\6\3\0\4\6\1\216"+
    "\22\6\26\0\1\6\1\0\2\6\3\0\13\6\1\217"+
    "\13\6\26\0\1\6\1\0\2\6\3\0\20\6\1\220"+
    "\6\6\26\0\1\6\1\0\2\6\3\0\13\6\1\221"+
    "\13\6\26\0\1\6\1\0\2\6\3\0\2\6\1\222"+
    "\24\6\26\0\1\6\1\0\2\6\3\0\26\6\1\223"+
    "\26\0\1\6\1\0\2\6\3\0\6\6\1\224\20\6"+
    "\26\0\1\6\1\0\2\6\3\0\4\6\1\225\22\6"+
    "\26\0\1\6\1\0\2\6\3\0\10\6\1\226\16\6"+
    "\26\0\1\6\1\0\2\6\3\0\10\6\1\227\16\6"+
    "\26\0\1\6\1\0\2\6\3\0\27\6\1\230\25\0"+
    "\1\6\1\0\2\6\3\0\7\6\1\231\17\6\46\0"+
    "\1\232\43\0\1\6\1\0\2\6\3\0\10\6\1\233"+
    "\16\6\57\0\1\234\57\0\1\235\74\0\1\236\57\0"+
    "\1\237\47\0\1\240\57\0\1\241\64\0\1\242\75\0"+
    "\1\243\57\0\1\244\55\0\1\245\44\0";

  /** 
   * The transition table of the DFA
   */
  private static final int yytrans [] = yy_unpack();


  /* error codes */
  private static final int YY_UNKNOWN_ERROR = 0;
  private static final int YY_ILLEGAL_STATE = 1;
  private static final int YY_NO_MATCH = 2;
  private static final int YY_PUSHBACK_2BIG = 3;

  /* error messages for the codes above */
  private static final String YY_ERROR_MSG[] = {
    "Unkown internal scanner error",
    "Internal error: unknown state",
    "Error: could not match input",
    "Error: pushback value was too large"
  };

  /**
   * YY_ATTRIBUTE[aState] contains the attributes of state <code>aState</code>
   */
  private static final byte YY_ATTRIBUTE[] = {
     0,  0,  1,  1,  9,  1,  1,  9,  1,  1,  1,  1,  1,  1,  1,  1, 
     1,  1,  1,  1,  1,  1,  9,  9,  9,  9,  9,  9,  9,  9,  9,  1, 
     9,  9,  1,  1,  1,  0,  0,  1,  1,  9,  9,  0,  0,  0,  1,  1, 
     1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1, 
     1,  1,  1,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9, 
     9,  9,  1,  9,  0,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1, 
     1,  1,  1,  1,  1,  1,  1,  1,  1,  0,  1,  1,  1,  1,  1,  1, 
     1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1, 
     1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1, 
     1,  1,  1,  1,  1,  1,  1,  0,  1,  0,  1,  0,  0,  0,  0,  0, 
     0,  0,  0,  0,  9
  };

  /** the input device */
  private java.io.Reader yy_reader;

  /** the current state of the DFA */
  private int yy_state;

  /** the current lexical state */
  private int yy_lexical_state = YYINITIAL;

  /** this buffer contains the current text to be matched and is
      the source of the yytext() string */
  private char yy_buffer[] = new char[YY_BUFFERSIZE];

  /** the textposition at the last accepting state */
  private int yy_markedPos;

  /** the textposition at the last state to be included in yytext */
  private int yy_pushbackPos;

  /** the current text position in the buffer */
  private int yy_currentPos;

  /** startRead marks the beginning of the yytext() string in the buffer */
  private int yy_startRead;

  /** endRead marks the last character in the buffer, that has been read
      from input */
  private int yy_endRead;

  /** number of newlines encountered up to the start of the matched text */
  private int yyline;

  /** the number of characters up to the start of the matched text */
  private int yychar;

  /**
   * the number of characters from the last newline up to the start of the 
   * matched text
   */
  private int yycolumn; 

  /** 
   * yy_atBOL == true <=> the scanner is currently at the beginning of a line
   */
  private boolean yy_atBOL = true;

  /** yy_atEOF == true <=> the scanner is at the EOF */
  private boolean yy_atEOF;

  /** denotes if the user-EOF-code has already been executed */
  private boolean yy_eof_done;

  /* user code: */
	StringBuffer string = new StringBuffer();
    private static int num_nested_comments = 0;
    
    private Symbol symbol(int sym) 
    {
        return new Symbol(sym, yyline+1, yycolumn+1);
    }
 
    private Symbol symbol(int sym, Object val) 
    {
        return new Symbol(sym, yyline+1, yycolumn+1, val);
    }
 
    private void error(String message) 
    {
        System.out.println("You messed up at line "+(yyline+1)+", column "+(yycolumn+1)+" : "+message);
    }


  /**
   * Creates a new scanner
   * There is also a java.io.InputStream version of this constructor.
   *
   * @param   in  the java.io.Reader to read input from.
   */
  Lexer(java.io.Reader in) {
    this.yy_reader = in;
  }

  /**
   * Creates a new scanner.
   * There is also java.io.Reader version of this constructor.
   *
   * @param   in  the java.io.Inputstream to read input from.
   */
  Lexer(java.io.InputStream in) {
    this(new java.io.InputStreamReader(in));
  }

  /** 
   * Unpacks the split, compressed DFA transition table.
   *
   * @return the unpacked transition table
   */
  private static int [] yy_unpack() {
    int [] trans = new int[5876];
    int offset = 0;
    offset = yy_unpack(yy_packed0, offset, trans);
    return trans;
  }

  /** 
   * Unpacks the compressed DFA transition table.
   *
   * @param packed   the packed transition table
   * @return         the index of the last entry
   */
  private static int yy_unpack(String packed, int offset, int [] trans) {
    int i = 0;       /* index in packed string  */
    int j = offset;  /* index in unpacked array */
    int l = packed.length();
    while (i < l) {
      int count = packed.charAt(i++);
      int value = packed.charAt(i++);
      value--;
      do trans[j++] = value; while (--count > 0);
    }
    return j;
  }


  /**
   * Refills the input buffer.
   *
   * @return      <code>false</code>, iff there was new input.
   * 
   * @exception   IOException  if any I/O-Error occurs
   */
  private boolean yy_refill() throws java.io.IOException {

    /* first: make room (if you can) */
    if (yy_startRead > 0) {
      System.arraycopy(yy_buffer, yy_startRead, 
                       yy_buffer, 0, 
                       yy_endRead-yy_startRead);

      /* translate stored positions */
      yy_endRead-= yy_startRead;
      yy_currentPos-= yy_startRead;
      yy_markedPos-= yy_startRead;
      yy_pushbackPos-= yy_startRead;
      yy_startRead = 0;
    }

    /* is the buffer big enough? */
    if (yy_currentPos >= yy_buffer.length) {
      /* if not: blow it up */
      char newBuffer[] = new char[yy_currentPos*2];
      System.arraycopy(yy_buffer, 0, newBuffer, 0, yy_buffer.length);
      yy_buffer = newBuffer;
    }

    /* finally: fill the buffer with new input */
    int numRead = yy_reader.read(yy_buffer, yy_endRead, 
                                            yy_buffer.length-yy_endRead);

    if (numRead < 0) {
      return true;
    }
    else {
      yy_endRead+= numRead;  
      return false;
    }
  }


  /**
   * Closes the input stream.
   */
  public final void yyclose() throws java.io.IOException {
    yy_atEOF = true;            /* indicate end of file */
    yy_endRead = yy_startRead;  /* invalidate buffer    */

    if (yy_reader != null)
      yy_reader.close();
  }


  /**
   * Closes the current stream, and resets the
   * scanner to read from a new input stream.
   *
   * All internal variables are reset, the old input stream 
   * <b>cannot</b> be reused (internal buffer is discarded and lost).
   * Lexical state is set to <tt>YY_INITIAL</tt>.
   *
   * @param reader   the new input stream 
   */
  public final void yyreset(java.io.Reader reader) throws java.io.IOException {
    yyclose();
    yy_reader = reader;
    yy_atBOL  = true;
    yy_atEOF  = false;
    yy_endRead = yy_startRead = 0;
    yy_currentPos = yy_markedPos = yy_pushbackPos = 0;
    yyline = yychar = yycolumn = 0;
    yy_lexical_state = YYINITIAL;
  }


  /**
   * Returns the current lexical state.
   */
  public final int yystate() {
    return yy_lexical_state;
  }


  /**
   * Enters a new lexical state
   *
   * @param newState the new lexical state
   */
  public final void yybegin(int newState) {
    yy_lexical_state = newState;
  }


  /**
   * Returns the text matched by the current regular expression.
   */
  public final String yytext() {
    return new String( yy_buffer, yy_startRead, yy_markedPos-yy_startRead );
  }


  /**
   * Returns the character at position <tt>pos</tt> from the 
   * matched text. 
   * 
   * It is equivalent to yytext().charAt(pos), but faster
   *
   * @param pos the position of the character to fetch. 
   *            A value from 0 to yylength()-1.
   *
   * @return the character at position pos
   */
  public final char yycharat(int pos) {
    return yy_buffer[yy_startRead+pos];
  }


  /**
   * Returns the length of the matched text region.
   */
  public final int yylength() {
    return yy_markedPos-yy_startRead;
  }


  /**
   * Reports an error that occured while scanning.
   *
   * In a wellformed scanner (no or only correct usage of 
   * yypushback(int) and a match-all fallback rule) this method 
   * will only be called with things that "Can't Possibly Happen".
   * If this method is called, something is seriously wrong
   * (e.g. a JFlex bug producing a faulty scanner etc.).
   *
   * Usual syntax/scanner level error handling should be done
   * in error fallback rules.
   *
   * @param   errorCode  the code of the errormessage to display
   */
  private void yy_ScanError(int errorCode) {
    String message;
    try {
      message = YY_ERROR_MSG[errorCode];
    }
    catch (ArrayIndexOutOfBoundsException e) {
      message = YY_ERROR_MSG[YY_UNKNOWN_ERROR];
    }

    throw new Error(message);
  } 


  /**
   * Pushes the specified amount of characters back into the input stream.
   *
   * They will be read again by then next call of the scanning method
   *
   * @param number  the number of characters to be read again.
   *                This number must not be greater than yylength()!
   */
  private void yypushback(int number)  {
    if ( number > yylength() )
      yy_ScanError(YY_PUSHBACK_2BIG);

    yy_markedPos -= number;
  }


  /**
   * Contains user EOF-code, which will be executed exactly once,
   * when the end of file is reached
   */
  private void yy_do_eof() throws java.io.IOException {
    if (!yy_eof_done) {
      yy_eof_done = true;
      yyclose();
    }
  }


  /**
   * Resumes scanning until the next regular expression is matched,
   * the end of input is encountered or an I/O-Error occurs.
   *
   * @return      the next token
   * @exception   IOException  if any I/O-Error occurs
   */
  public java_cup.runtime.Symbol next_token() throws java.io.IOException {
    int yy_input;
    int yy_action;

    // cached fields:
    int yy_currentPos_l;
    int yy_startRead_l;
    int yy_markedPos_l;
    int yy_endRead_l = yy_endRead;
    char [] yy_buffer_l = yy_buffer;
    char [] yycmap_l = yycmap;

    int [] yytrans_l = yytrans;
    int [] yy_rowMap_l = yy_rowMap;
    byte [] yy_attr_l = YY_ATTRIBUTE;

    while (true) {
      yy_markedPos_l = yy_markedPos;

      boolean yy_r = false;
      for (yy_currentPos_l = yy_startRead; yy_currentPos_l < yy_markedPos_l;
                                                             yy_currentPos_l++) {
        switch (yy_buffer_l[yy_currentPos_l]) {
        case '\u000B':
        case '\u000C':
        case '\u0085':
        case '\u2028':
        case '\u2029':
          yyline++;
          yycolumn = 0;
          yy_r = false;
          break;
        case '\r':
          yyline++;
          yycolumn = 0;
          yy_r = true;
          break;
        case '\n':
          if (yy_r)
            yy_r = false;
          else {
            yyline++;
            yycolumn = 0;
          }
          break;
        default:
          yy_r = false;
          yycolumn++;
        }
      }

      if (yy_r) {
        // peek one character ahead if it is \n (if we have counted one line too much)
        boolean yy_peek;
        if (yy_markedPos_l < yy_endRead_l)
          yy_peek = yy_buffer_l[yy_markedPos_l] == '\n';
        else if (yy_atEOF)
          yy_peek = false;
        else {
          boolean eof = yy_refill();
          yy_markedPos_l = yy_markedPos;
          yy_buffer_l = yy_buffer;
          if (eof) 
            yy_peek = false;
          else 
            yy_peek = yy_buffer_l[yy_markedPos_l] == '\n';
        }
        if (yy_peek) yyline--;
      }
      yy_action = -1;

      yy_startRead_l = yy_currentPos_l = yy_currentPos = 
                       yy_startRead = yy_markedPos_l;

      yy_state = yy_lexical_state;


      yy_forAction: {
        while (true) {

          if (yy_currentPos_l < yy_endRead_l)
            yy_input = yy_buffer_l[yy_currentPos_l++];
          else if (yy_atEOF) {
            yy_input = YYEOF;
            break yy_forAction;
          }
          else {
            // store back cached positions
            yy_currentPos  = yy_currentPos_l;
            yy_markedPos   = yy_markedPos_l;
            boolean eof = yy_refill();
            // get translated positions and possibly new buffer
            yy_currentPos_l  = yy_currentPos;
            yy_markedPos_l   = yy_markedPos;
            yy_buffer_l      = yy_buffer;
            yy_endRead_l     = yy_endRead;
            if (eof) {
              yy_input = YYEOF;
              break yy_forAction;
            }
            else {
              yy_input = yy_buffer_l[yy_currentPos_l++];
            }
          }
          int yy_next = yytrans_l[ yy_rowMap_l[yy_state] + yycmap_l[yy_input] ];
          if (yy_next == -1) break yy_forAction;
          yy_state = yy_next;

          int yy_attributes = yy_attr_l[yy_state];
          if ( (yy_attributes & 1) == 1 ) {
            yy_action = yy_state; 
            yy_markedPos_l = yy_currentPos_l; 
            if ( (yy_attributes & 8) == 8 ) break yy_forAction;
          }

        }
      }

      // store back cached position
      yy_markedPos = yy_markedPos_l;

      switch (yy_action) {

        case 90: 
          { return symbol(INTTYPE_TOK);  }
        case 166: break;
        case 154: 
          { return symbol(BEGINVARS_TOK);  }
        case 167: break;
        case 150: 
          { return symbol(EXTENDS_TOK);  }
        case 168: break;
        case 149: 
          { return symbol(ENDVARS_TOK);  }
        case 169: break;
        case 29: 
          { return symbol(SEMICOLON_TOK);  }
        case 170: break;
        case 148: 
          { return symbol(BOOLTYPE_TOK);  }
        case 171: break;
        case 39: 
          {  string.append( yytext() );  }
        case 172: break;
        case 42: 
          {  yybegin(YYINITIAL); return symbol(STRCONST_TOK, string.toString());  }
        case 173: break;
        case 82: 
        case 83: 
          {   }
        case 174: break;
        case 2: 
          {   }
        case 175: break;
        case 73: 
          {  throw new RuntimeException("Illegal escape sequence \""+yytext()+"\"");  }
        case 176: break;
        case 3: 
          { return symbol(INTCONST_TOK, new Integer(yytext()));  }
        case 177: break;
        case 164: 
          { return symbol(PRINT_TOK);  }
        case 178: break;
        case 145: 
          { return symbol(STRING_TOK);  }
        case 179: break;
        case 144: 
          { return symbol(PUBLIC_TOK);  }
        case 180: break;
        case 143: 
          { return symbol(LENGTH_TOK);  }
        case 181: break;
        case 142: 
          { return symbol(STATIC_TOK);  }
        case 182: break;
        case 141: 
          { return symbol(RETURN_TOK);  }
        case 183: break;
        case 133: 
          { return symbol(WHILE_TOK);  }
        case 184: break;
        case 132: 
          { return symbol(FALSE_TOK);  }
        case 185: break;
        case 131: 
          { return symbol(CLASS_TOK);  }
        case 186: break;
        case 30: 
          { return symbol(COMMA_TOK);  }
        case 187: break;
        case 26: 
          { return symbol(RBRACE_TOK);  }
        case 188: break;
        case 25: 
          { return symbol(LBRACE_TOK);  }
        case 189: break;
        case 24: 
          { return symbol(RPAREN_TOK);  }
        case 190: break;
        case 23: 
          { return symbol(LPAREN_TOK);  }
        case 191: break;
        case 33: 
          { return symbol(MINUS_TOK);  }
        case 192: break;
        case 36: 
          { return symbol(ASSIGN_TOK);  }
        case 193: break;
        case 40: 
        case 41: 
          {  throw new RuntimeException("Unterminated string at end of line");  }
        case 194: break;
        case 81: 
          {  string.append( '\'' );  }
        case 195: break;
        case 80: 
          {  string.append( '\f' );  }
        case 196: break;
        case 79: 
          {  string.append( '\t' );  }
        case 197: break;
        case 78: 
          {  string.append( '\r' );  }
        case 198: break;
        case 77: 
          {  string.append( '\n' );  }
        case 199: break;
        case 74: 
          {  string.append( '\"' );  }
        case 200: break;
        case 75: 
          {  string.append( '\\' );  }
        case 201: break;
        case 76: 
          {  string.append( '\b' );  }
        case 202: break;
        case 4: 
          { yybegin(STRING); string.setLength(0); }
        case 203: break;
        case 34: 
          { return symbol(GT_TOK);  }
        case 204: break;
        case 35: 
          { return symbol(LT_TOK);  }
        case 205: break;
        case 52: 
          { return symbol(IF_TOK);  }
        case 206: break;
        case 70: 
          { return symbol(EQ_TOK);  }
        case 207: break;
        case 118: 
          { return symbol(THIS_TOK);  }
        case 208: break;
        case 117: 
          { return symbol(TRUE_TOK);  }
        case 209: break;
        case 112: 
          { return symbol(VOID_TOK);  }
        case 210: break;
        case 111: 
          { return symbol(NULL_TOK);  }
        case 211: break;
        case 109: 
          { return symbol(ELSE_TOK);  }
        case 212: break;
        case 91: 
          { return symbol(NEW_TOK);  }
        case 213: break;
        case 32: 
          { return symbol(PLUS_TOK);  }
        case 214: break;
        case 31: 
          { return symbol(BANG_TOK);  }
        case 215: break;
        case 6: 
          { return symbol(DIV_TOK);  }
        case 216: break;
        case 7: 
          { return symbol(MUL_TOK);  }
        case 217: break;
        case 22: 
          { return symbol(DOT_TOK);  }
        case 218: break;
        case 67: 
          { return symbol(NEQ_TOK);  }
        case 219: break;
        case 68: 
          { return symbol(GTEQ_TOK);  }
        case 220: break;
        case 69: 
          { return symbol(LTEQ_TOK);  }
        case 221: break;
        case 71: 
          { return symbol(AND_TOK);  }
        case 222: break;
        case 72: 
          { return symbol(OR_TOK);   }
        case 223: break;
        case 5: 
        case 8: 
        case 9: 
        case 10: 
        case 11: 
        case 12: 
        case 13: 
        case 14: 
        case 15: 
        case 16: 
        case 17: 
        case 18: 
        case 19: 
        case 20: 
        case 21: 
        case 46: 
        case 47: 
        case 48: 
        case 49: 
        case 50: 
        case 51: 
        case 53: 
        case 54: 
        case 55: 
        case 56: 
        case 57: 
        case 58: 
        case 59: 
        case 60: 
        case 61: 
        case 62: 
        case 63: 
        case 64: 
        case 65: 
        case 66: 
        case 85: 
        case 86: 
        case 87: 
        case 88: 
        case 89: 
        case 92: 
        case 93: 
        case 94: 
        case 95: 
        case 96: 
        case 97: 
        case 98: 
        case 99: 
        case 100: 
        case 101: 
        case 102: 
        case 103: 
        case 104: 
        case 106: 
        case 107: 
        case 108: 
        case 110: 
        case 113: 
        case 114: 
        case 115: 
        case 116: 
        case 119: 
        case 120: 
        case 121: 
        case 122: 
        case 123: 
        case 124: 
        case 125: 
        case 126: 
        case 127: 
        case 128: 
        case 129: 
        case 130: 
        case 134: 
        case 135: 
        case 136: 
        case 137: 
        case 138: 
        case 139: 
        case 140: 
        case 146: 
        case 147: 
        case 152: 
          { return symbol(ID_TOK, yytext());  }
        case 224: break;
        case 28: 
          { return symbol(RBRACKET_TOK);  }
        case 225: break;
        case 27: 
          { return symbol(LBRACKET_TOK);  }
        case 226: break;
        default: 
          if (yy_input == YYEOF && yy_startRead == yy_currentPos) {
            yy_atEOF = true;
            yy_do_eof();
              { return new java_cup.runtime.Symbol(sym.EOF); }
          } 
          else {
            yy_ScanError(YY_NO_MATCH);
          }
      }
    }
  }


}
