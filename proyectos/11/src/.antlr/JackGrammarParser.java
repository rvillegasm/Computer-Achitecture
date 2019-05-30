// Generated from /home/rvillegasm/src/st254/254srvillegasm/proyectos/10/src/JackGrammar.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class JackGrammarParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, T__37=38, 
		T__38=39, T__39=40, INTEGERCONSTANT=41, STRINGCONSTANT=42, IDENTIFIER=43, 
		WHITESPACE=44, INLINECOMENT=45, DOCCOMENT=46;
	public static final int
		RULE_classNT = 0, RULE_classVarDecNT = 1, RULE_typeNT = 2, RULE_subroutineDecNT = 3, 
		RULE_parameterListNT = 4, RULE_subroutineBodyNT = 5, RULE_varDecNT = 6, 
		RULE_classNameNT = 7, RULE_subroutineNameNT = 8, RULE_varNameNT = 9, RULE_statementsNT = 10, 
		RULE_statementNT = 11, RULE_letStatementNT = 12, RULE_ifStatementNT = 13, 
		RULE_whileStatementNT = 14, RULE_doStatementNT = 15, RULE_returnStatementNT = 16, 
		RULE_expressionNT = 17, RULE_termNT = 18, RULE_subroutineCallNT = 19, 
		RULE_expressionListNT = 20, RULE_opNT = 21, RULE_unaryOpNT = 22, RULE_keywordConstantNT = 23;
	public static final String[] ruleNames = {
		"classNT", "classVarDecNT", "typeNT", "subroutineDecNT", "parameterListNT", 
		"subroutineBodyNT", "varDecNT", "classNameNT", "subroutineNameNT", "varNameNT", 
		"statementsNT", "statementNT", "letStatementNT", "ifStatementNT", "whileStatementNT", 
		"doStatementNT", "returnStatementNT", "expressionNT", "termNT", "subroutineCallNT", 
		"expressionListNT", "opNT", "unaryOpNT", "keywordConstantNT"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'class'", "'{'", "'}'", "'static'", "'field'", "','", "';'", "'int'", 
		"'char'", "'boolean'", "'constructor'", "'function'", "'method'", "'void'", 
		"'('", "')'", "'var'", "'let'", "'['", "']'", "'='", "'if'", "'else'", 
		"'while'", "'do'", "'return'", "'.'", "'+'", "'-'", "'*'", "'/'", "'&'", 
		"'|'", "'<'", "'>'", "'~'", "'true'", "'false'", "'null'", "'this'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, null, "INTEGERCONSTANT", "STRINGCONSTANT", "IDENTIFIER", 
		"WHITESPACE", "INLINECOMENT", "DOCCOMENT"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "JackGrammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public JackGrammarParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class ClassNTContext extends ParserRuleContext {
		public ClassNameNTContext classNameNT() {
			return getRuleContext(ClassNameNTContext.class,0);
		}
		public List<ClassVarDecNTContext> classVarDecNT() {
			return getRuleContexts(ClassVarDecNTContext.class);
		}
		public ClassVarDecNTContext classVarDecNT(int i) {
			return getRuleContext(ClassVarDecNTContext.class,i);
		}
		public List<SubroutineDecNTContext> subroutineDecNT() {
			return getRuleContexts(SubroutineDecNTContext.class);
		}
		public SubroutineDecNTContext subroutineDecNT(int i) {
			return getRuleContext(SubroutineDecNTContext.class,i);
		}
		public ClassNTContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classNT; }
	}

	public final ClassNTContext classNT() throws RecognitionException {
		ClassNTContext _localctx = new ClassNTContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_classNT);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			match(T__0);
			setState(49);
			classNameNT();
			setState(50);
			match(T__1);
			setState(54);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__3 || _la==T__4) {
				{
				{
				setState(51);
				classVarDecNT();
				}
				}
				setState(56);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(60);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__10) | (1L << T__11) | (1L << T__12))) != 0)) {
				{
				{
				setState(57);
				subroutineDecNT();
				}
				}
				setState(62);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(63);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClassVarDecNTContext extends ParserRuleContext {
		public TypeNTContext typeNT() {
			return getRuleContext(TypeNTContext.class,0);
		}
		public List<VarNameNTContext> varNameNT() {
			return getRuleContexts(VarNameNTContext.class);
		}
		public VarNameNTContext varNameNT(int i) {
			return getRuleContext(VarNameNTContext.class,i);
		}
		public ClassVarDecNTContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classVarDecNT; }
	}

	public final ClassVarDecNTContext classVarDecNT() throws RecognitionException {
		ClassVarDecNTContext _localctx = new ClassVarDecNTContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_classVarDecNT);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(65);
			_la = _input.LA(1);
			if ( !(_la==T__3 || _la==T__4) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(66);
			typeNT();
			setState(67);
			varNameNT();
			setState(72);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__5) {
				{
				{
				setState(68);
				match(T__5);
				setState(69);
				varNameNT();
				}
				}
				setState(74);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(75);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypeNTContext extends ParserRuleContext {
		public ClassNameNTContext classNameNT() {
			return getRuleContext(ClassNameNTContext.class,0);
		}
		public TypeNTContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeNT; }
	}

	public final TypeNTContext typeNT() throws RecognitionException {
		TypeNTContext _localctx = new TypeNTContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_typeNT);
		try {
			setState(81);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__7:
				enterOuterAlt(_localctx, 1);
				{
				setState(77);
				match(T__7);
				}
				break;
			case T__8:
				enterOuterAlt(_localctx, 2);
				{
				setState(78);
				match(T__8);
				}
				break;
			case T__9:
				enterOuterAlt(_localctx, 3);
				{
				setState(79);
				match(T__9);
				}
				break;
			case IDENTIFIER:
				enterOuterAlt(_localctx, 4);
				{
				setState(80);
				classNameNT();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SubroutineDecNTContext extends ParserRuleContext {
		public SubroutineNameNTContext subroutineNameNT() {
			return getRuleContext(SubroutineNameNTContext.class,0);
		}
		public ParameterListNTContext parameterListNT() {
			return getRuleContext(ParameterListNTContext.class,0);
		}
		public SubroutineBodyNTContext subroutineBodyNT() {
			return getRuleContext(SubroutineBodyNTContext.class,0);
		}
		public TypeNTContext typeNT() {
			return getRuleContext(TypeNTContext.class,0);
		}
		public SubroutineDecNTContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subroutineDecNT; }
	}

	public final SubroutineDecNTContext subroutineDecNT() throws RecognitionException {
		SubroutineDecNTContext _localctx = new SubroutineDecNTContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_subroutineDecNT);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__10) | (1L << T__11) | (1L << T__12))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(86);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__13:
				{
				setState(84);
				match(T__13);
				}
				break;
			case T__7:
			case T__8:
			case T__9:
			case IDENTIFIER:
				{
				setState(85);
				typeNT();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(88);
			subroutineNameNT();
			setState(89);
			match(T__14);
			setState(90);
			parameterListNT();
			setState(91);
			match(T__15);
			setState(92);
			subroutineBodyNT();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParameterListNTContext extends ParserRuleContext {
		public List<TypeNTContext> typeNT() {
			return getRuleContexts(TypeNTContext.class);
		}
		public TypeNTContext typeNT(int i) {
			return getRuleContext(TypeNTContext.class,i);
		}
		public List<VarNameNTContext> varNameNT() {
			return getRuleContexts(VarNameNTContext.class);
		}
		public VarNameNTContext varNameNT(int i) {
			return getRuleContext(VarNameNTContext.class,i);
		}
		public ParameterListNTContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameterListNT; }
	}

	public final ParameterListNTContext parameterListNT() throws RecognitionException {
		ParameterListNTContext _localctx = new ParameterListNTContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_parameterListNT);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(106);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << IDENTIFIER))) != 0)) {
				{
				{
				setState(94);
				typeNT();
				setState(95);
				varNameNT();
				}
				setState(103);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__5) {
					{
					{
					setState(97);
					match(T__5);
					setState(98);
					typeNT();
					setState(99);
					varNameNT();
					}
					}
					setState(105);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SubroutineBodyNTContext extends ParserRuleContext {
		public StatementsNTContext statementsNT() {
			return getRuleContext(StatementsNTContext.class,0);
		}
		public List<VarDecNTContext> varDecNT() {
			return getRuleContexts(VarDecNTContext.class);
		}
		public VarDecNTContext varDecNT(int i) {
			return getRuleContext(VarDecNTContext.class,i);
		}
		public SubroutineBodyNTContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subroutineBodyNT; }
	}

	public final SubroutineBodyNTContext subroutineBodyNT() throws RecognitionException {
		SubroutineBodyNTContext _localctx = new SubroutineBodyNTContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_subroutineBodyNT);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			match(T__1);
			setState(112);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__16) {
				{
				{
				setState(109);
				varDecNT();
				}
				}
				setState(114);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(115);
			statementsNT();
			setState(116);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarDecNTContext extends ParserRuleContext {
		public TypeNTContext typeNT() {
			return getRuleContext(TypeNTContext.class,0);
		}
		public List<VarNameNTContext> varNameNT() {
			return getRuleContexts(VarNameNTContext.class);
		}
		public VarNameNTContext varNameNT(int i) {
			return getRuleContext(VarNameNTContext.class,i);
		}
		public VarDecNTContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varDecNT; }
	}

	public final VarDecNTContext varDecNT() throws RecognitionException {
		VarDecNTContext _localctx = new VarDecNTContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_varDecNT);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(118);
			match(T__16);
			setState(119);
			typeNT();
			setState(120);
			varNameNT();
			setState(125);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__5) {
				{
				{
				setState(121);
				match(T__5);
				setState(122);
				varNameNT();
				}
				}
				setState(127);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(128);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ClassNameNTContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(JackGrammarParser.IDENTIFIER, 0); }
		public ClassNameNTContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classNameNT; }
	}

	public final ClassNameNTContext classNameNT() throws RecognitionException {
		ClassNameNTContext _localctx = new ClassNameNTContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_classNameNT);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(130);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SubroutineNameNTContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(JackGrammarParser.IDENTIFIER, 0); }
		public SubroutineNameNTContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subroutineNameNT; }
	}

	public final SubroutineNameNTContext subroutineNameNT() throws RecognitionException {
		SubroutineNameNTContext _localctx = new SubroutineNameNTContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_subroutineNameNT);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(132);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarNameNTContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(JackGrammarParser.IDENTIFIER, 0); }
		public VarNameNTContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varNameNT; }
	}

	public final VarNameNTContext varNameNT() throws RecognitionException {
		VarNameNTContext _localctx = new VarNameNTContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_varNameNT);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(134);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementsNTContext extends ParserRuleContext {
		public List<StatementNTContext> statementNT() {
			return getRuleContexts(StatementNTContext.class);
		}
		public StatementNTContext statementNT(int i) {
			return getRuleContext(StatementNTContext.class,i);
		}
		public StatementsNTContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statementsNT; }
	}

	public final StatementsNTContext statementsNT() throws RecognitionException {
		StatementsNTContext _localctx = new StatementsNTContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_statementsNT);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(139);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__17) | (1L << T__21) | (1L << T__23) | (1L << T__24) | (1L << T__25))) != 0)) {
				{
				{
				setState(136);
				statementNT();
				}
				}
				setState(141);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementNTContext extends ParserRuleContext {
		public LetStatementNTContext letStatementNT() {
			return getRuleContext(LetStatementNTContext.class,0);
		}
		public IfStatementNTContext ifStatementNT() {
			return getRuleContext(IfStatementNTContext.class,0);
		}
		public WhileStatementNTContext whileStatementNT() {
			return getRuleContext(WhileStatementNTContext.class,0);
		}
		public DoStatementNTContext doStatementNT() {
			return getRuleContext(DoStatementNTContext.class,0);
		}
		public ReturnStatementNTContext returnStatementNT() {
			return getRuleContext(ReturnStatementNTContext.class,0);
		}
		public StatementNTContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statementNT; }
	}

	public final StatementNTContext statementNT() throws RecognitionException {
		StatementNTContext _localctx = new StatementNTContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_statementNT);
		try {
			setState(147);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__17:
				enterOuterAlt(_localctx, 1);
				{
				setState(142);
				letStatementNT();
				}
				break;
			case T__21:
				enterOuterAlt(_localctx, 2);
				{
				setState(143);
				ifStatementNT();
				}
				break;
			case T__23:
				enterOuterAlt(_localctx, 3);
				{
				setState(144);
				whileStatementNT();
				}
				break;
			case T__24:
				enterOuterAlt(_localctx, 4);
				{
				setState(145);
				doStatementNT();
				}
				break;
			case T__25:
				enterOuterAlt(_localctx, 5);
				{
				setState(146);
				returnStatementNT();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LetStatementNTContext extends ParserRuleContext {
		public VarNameNTContext varNameNT() {
			return getRuleContext(VarNameNTContext.class,0);
		}
		public List<ExpressionNTContext> expressionNT() {
			return getRuleContexts(ExpressionNTContext.class);
		}
		public ExpressionNTContext expressionNT(int i) {
			return getRuleContext(ExpressionNTContext.class,i);
		}
		public LetStatementNTContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_letStatementNT; }
	}

	public final LetStatementNTContext letStatementNT() throws RecognitionException {
		LetStatementNTContext _localctx = new LetStatementNTContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_letStatementNT);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(149);
			match(T__17);
			setState(150);
			varNameNT();
			setState(155);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__18) {
				{
				setState(151);
				match(T__18);
				setState(152);
				expressionNT();
				setState(153);
				match(T__19);
				}
			}

			setState(157);
			match(T__20);
			setState(158);
			expressionNT();
			setState(159);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class IfStatementNTContext extends ParserRuleContext {
		public ExpressionNTContext expressionNT() {
			return getRuleContext(ExpressionNTContext.class,0);
		}
		public List<StatementsNTContext> statementsNT() {
			return getRuleContexts(StatementsNTContext.class);
		}
		public StatementsNTContext statementsNT(int i) {
			return getRuleContext(StatementsNTContext.class,i);
		}
		public IfStatementNTContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStatementNT; }
	}

	public final IfStatementNTContext ifStatementNT() throws RecognitionException {
		IfStatementNTContext _localctx = new IfStatementNTContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_ifStatementNT);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(161);
			match(T__21);
			setState(162);
			match(T__14);
			setState(163);
			expressionNT();
			setState(164);
			match(T__15);
			setState(165);
			match(T__1);
			setState(166);
			statementsNT();
			setState(167);
			match(T__2);
			setState(173);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__22) {
				{
				setState(168);
				match(T__22);
				setState(169);
				match(T__1);
				setState(170);
				statementsNT();
				setState(171);
				match(T__2);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class WhileStatementNTContext extends ParserRuleContext {
		public ExpressionNTContext expressionNT() {
			return getRuleContext(ExpressionNTContext.class,0);
		}
		public StatementsNTContext statementsNT() {
			return getRuleContext(StatementsNTContext.class,0);
		}
		public WhileStatementNTContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileStatementNT; }
	}

	public final WhileStatementNTContext whileStatementNT() throws RecognitionException {
		WhileStatementNTContext _localctx = new WhileStatementNTContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_whileStatementNT);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(175);
			match(T__23);
			setState(176);
			match(T__14);
			setState(177);
			expressionNT();
			setState(178);
			match(T__15);
			setState(179);
			match(T__1);
			setState(180);
			statementsNT();
			setState(181);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DoStatementNTContext extends ParserRuleContext {
		public SubroutineCallNTContext subroutineCallNT() {
			return getRuleContext(SubroutineCallNTContext.class,0);
		}
		public DoStatementNTContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_doStatementNT; }
	}

	public final DoStatementNTContext doStatementNT() throws RecognitionException {
		DoStatementNTContext _localctx = new DoStatementNTContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_doStatementNT);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(183);
			match(T__24);
			setState(184);
			subroutineCallNT();
			setState(185);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ReturnStatementNTContext extends ParserRuleContext {
		public ExpressionNTContext expressionNT() {
			return getRuleContext(ExpressionNTContext.class,0);
		}
		public ReturnStatementNTContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnStatementNT; }
	}

	public final ReturnStatementNTContext returnStatementNT() throws RecognitionException {
		ReturnStatementNTContext _localctx = new ReturnStatementNTContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_returnStatementNT);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(187);
			match(T__25);
			setState(189);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__14) | (1L << T__28) | (1L << T__35) | (1L << T__36) | (1L << T__37) | (1L << T__38) | (1L << T__39) | (1L << INTEGERCONSTANT) | (1L << STRINGCONSTANT) | (1L << IDENTIFIER))) != 0)) {
				{
				setState(188);
				expressionNT();
				}
			}

			setState(191);
			match(T__6);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionNTContext extends ParserRuleContext {
		public List<TermNTContext> termNT() {
			return getRuleContexts(TermNTContext.class);
		}
		public TermNTContext termNT(int i) {
			return getRuleContext(TermNTContext.class,i);
		}
		public List<OpNTContext> opNT() {
			return getRuleContexts(OpNTContext.class);
		}
		public OpNTContext opNT(int i) {
			return getRuleContext(OpNTContext.class,i);
		}
		public ExpressionNTContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressionNT; }
	}

	public final ExpressionNTContext expressionNT() throws RecognitionException {
		ExpressionNTContext _localctx = new ExpressionNTContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_expressionNT);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(193);
			termNT();
			setState(199);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__20) | (1L << T__27) | (1L << T__28) | (1L << T__29) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << T__33) | (1L << T__34))) != 0)) {
				{
				{
				setState(194);
				opNT();
				setState(195);
				termNT();
				}
				}
				setState(201);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TermNTContext extends ParserRuleContext {
		public TerminalNode INTEGERCONSTANT() { return getToken(JackGrammarParser.INTEGERCONSTANT, 0); }
		public TerminalNode STRINGCONSTANT() { return getToken(JackGrammarParser.STRINGCONSTANT, 0); }
		public KeywordConstantNTContext keywordConstantNT() {
			return getRuleContext(KeywordConstantNTContext.class,0);
		}
		public VarNameNTContext varNameNT() {
			return getRuleContext(VarNameNTContext.class,0);
		}
		public ExpressionNTContext expressionNT() {
			return getRuleContext(ExpressionNTContext.class,0);
		}
		public SubroutineCallNTContext subroutineCallNT() {
			return getRuleContext(SubroutineCallNTContext.class,0);
		}
		public UnaryOpNTContext unaryOpNT() {
			return getRuleContext(UnaryOpNTContext.class,0);
		}
		public TermNTContext termNT() {
			return getRuleContext(TermNTContext.class,0);
		}
		public TermNTContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_termNT; }
	}

	public final TermNTContext termNT() throws RecognitionException {
		TermNTContext _localctx = new TermNTContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_termNT);
		try {
			setState(219);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(202);
				match(INTEGERCONSTANT);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(203);
				match(STRINGCONSTANT);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(204);
				keywordConstantNT();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(205);
				varNameNT();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(206);
				varNameNT();
				setState(207);
				match(T__18);
				setState(208);
				expressionNT();
				setState(209);
				match(T__19);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(211);
				subroutineCallNT();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(212);
				match(T__14);
				setState(213);
				expressionNT();
				setState(214);
				match(T__15);
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(216);
				unaryOpNT();
				setState(217);
				termNT();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SubroutineCallNTContext extends ParserRuleContext {
		public SubroutineNameNTContext subroutineNameNT() {
			return getRuleContext(SubroutineNameNTContext.class,0);
		}
		public ExpressionListNTContext expressionListNT() {
			return getRuleContext(ExpressionListNTContext.class,0);
		}
		public ClassNameNTContext classNameNT() {
			return getRuleContext(ClassNameNTContext.class,0);
		}
		public VarNameNTContext varNameNT() {
			return getRuleContext(VarNameNTContext.class,0);
		}
		public SubroutineCallNTContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_subroutineCallNT; }
	}

	public final SubroutineCallNTContext subroutineCallNT() throws RecognitionException {
		SubroutineCallNTContext _localctx = new SubroutineCallNTContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_subroutineCallNT);
		try {
			setState(236);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(221);
				subroutineNameNT();
				setState(222);
				match(T__14);
				setState(223);
				expressionListNT();
				setState(224);
				match(T__15);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(228);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
				case 1:
					{
					setState(226);
					classNameNT();
					}
					break;
				case 2:
					{
					setState(227);
					varNameNT();
					}
					break;
				}
				setState(230);
				match(T__26);
				setState(231);
				subroutineNameNT();
				setState(232);
				match(T__14);
				setState(233);
				expressionListNT();
				setState(234);
				match(T__15);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionListNTContext extends ParserRuleContext {
		public List<ExpressionNTContext> expressionNT() {
			return getRuleContexts(ExpressionNTContext.class);
		}
		public ExpressionNTContext expressionNT(int i) {
			return getRuleContext(ExpressionNTContext.class,i);
		}
		public ExpressionListNTContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressionListNT; }
	}

	public final ExpressionListNTContext expressionListNT() throws RecognitionException {
		ExpressionListNTContext _localctx = new ExpressionListNTContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_expressionListNT);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(246);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__14) | (1L << T__28) | (1L << T__35) | (1L << T__36) | (1L << T__37) | (1L << T__38) | (1L << T__39) | (1L << INTEGERCONSTANT) | (1L << STRINGCONSTANT) | (1L << IDENTIFIER))) != 0)) {
				{
				setState(238);
				expressionNT();
				setState(243);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__5) {
					{
					{
					setState(239);
					match(T__5);
					setState(240);
					expressionNT();
					}
					}
					setState(245);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class OpNTContext extends ParserRuleContext {
		public OpNTContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opNT; }
	}

	public final OpNTContext opNT() throws RecognitionException {
		OpNTContext _localctx = new OpNTContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_opNT);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(248);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__20) | (1L << T__27) | (1L << T__28) | (1L << T__29) | (1L << T__30) | (1L << T__31) | (1L << T__32) | (1L << T__33) | (1L << T__34))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class UnaryOpNTContext extends ParserRuleContext {
		public UnaryOpNTContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unaryOpNT; }
	}

	public final UnaryOpNTContext unaryOpNT() throws RecognitionException {
		UnaryOpNTContext _localctx = new UnaryOpNTContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_unaryOpNT);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(250);
			_la = _input.LA(1);
			if ( !(_la==T__28 || _la==T__35) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class KeywordConstantNTContext extends ParserRuleContext {
		public KeywordConstantNTContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_keywordConstantNT; }
	}

	public final KeywordConstantNTContext keywordConstantNT() throws RecognitionException {
		KeywordConstantNTContext _localctx = new KeywordConstantNTContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_keywordConstantNT);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(252);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__36) | (1L << T__37) | (1L << T__38) | (1L << T__39))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\60\u0101\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\3\2\3\2\3\2\3\2\7\2\67\n\2\f\2\16\2:\13\2\3\2\7\2=\n\2\f\2\16\2@\13\2"+
		"\3\2\3\2\3\3\3\3\3\3\3\3\3\3\7\3I\n\3\f\3\16\3L\13\3\3\3\3\3\3\4\3\4\3"+
		"\4\3\4\5\4T\n\4\3\5\3\5\3\5\5\5Y\n\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\3\6\7\6h\n\6\f\6\16\6k\13\6\5\6m\n\6\3\7\3\7\7\7q\n\7\f"+
		"\7\16\7t\13\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\7\b~\n\b\f\b\16\b\u0081"+
		"\13\b\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\7\f\u008c\n\f\f\f\16\f\u008f"+
		"\13\f\3\r\3\r\3\r\3\r\3\r\5\r\u0096\n\r\3\16\3\16\3\16\3\16\3\16\3\16"+
		"\5\16\u009e\n\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\3\17\3\17\3\17\3\17\3\17\5\17\u00b0\n\17\3\20\3\20\3\20\3\20\3\20\3\20"+
		"\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\5\22\u00c0\n\22\3\22\3\22\3\23"+
		"\3\23\3\23\3\23\7\23\u00c8\n\23\f\23\16\23\u00cb\13\23\3\24\3\24\3\24"+
		"\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24"+
		"\5\24\u00de\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u00e7\n\25\3"+
		"\25\3\25\3\25\3\25\3\25\3\25\5\25\u00ef\n\25\3\26\3\26\3\26\7\26\u00f4"+
		"\n\26\f\26\16\26\u00f7\13\26\5\26\u00f9\n\26\3\27\3\27\3\30\3\30\3\31"+
		"\3\31\3\31\2\2\32\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\2"+
		"\7\3\2\6\7\3\2\r\17\4\2\27\27\36%\4\2\37\37&&\3\2\'*\2\u0107\2\62\3\2"+
		"\2\2\4C\3\2\2\2\6S\3\2\2\2\bU\3\2\2\2\nl\3\2\2\2\fn\3\2\2\2\16x\3\2\2"+
		"\2\20\u0084\3\2\2\2\22\u0086\3\2\2\2\24\u0088\3\2\2\2\26\u008d\3\2\2\2"+
		"\30\u0095\3\2\2\2\32\u0097\3\2\2\2\34\u00a3\3\2\2\2\36\u00b1\3\2\2\2 "+
		"\u00b9\3\2\2\2\"\u00bd\3\2\2\2$\u00c3\3\2\2\2&\u00dd\3\2\2\2(\u00ee\3"+
		"\2\2\2*\u00f8\3\2\2\2,\u00fa\3\2\2\2.\u00fc\3\2\2\2\60\u00fe\3\2\2\2\62"+
		"\63\7\3\2\2\63\64\5\20\t\2\648\7\4\2\2\65\67\5\4\3\2\66\65\3\2\2\2\67"+
		":\3\2\2\28\66\3\2\2\289\3\2\2\29>\3\2\2\2:8\3\2\2\2;=\5\b\5\2<;\3\2\2"+
		"\2=@\3\2\2\2><\3\2\2\2>?\3\2\2\2?A\3\2\2\2@>\3\2\2\2AB\7\5\2\2B\3\3\2"+
		"\2\2CD\t\2\2\2DE\5\6\4\2EJ\5\24\13\2FG\7\b\2\2GI\5\24\13\2HF\3\2\2\2I"+
		"L\3\2\2\2JH\3\2\2\2JK\3\2\2\2KM\3\2\2\2LJ\3\2\2\2MN\7\t\2\2N\5\3\2\2\2"+
		"OT\7\n\2\2PT\7\13\2\2QT\7\f\2\2RT\5\20\t\2SO\3\2\2\2SP\3\2\2\2SQ\3\2\2"+
		"\2SR\3\2\2\2T\7\3\2\2\2UX\t\3\2\2VY\7\20\2\2WY\5\6\4\2XV\3\2\2\2XW\3\2"+
		"\2\2YZ\3\2\2\2Z[\5\22\n\2[\\\7\21\2\2\\]\5\n\6\2]^\7\22\2\2^_\5\f\7\2"+
		"_\t\3\2\2\2`a\5\6\4\2ab\5\24\13\2bi\3\2\2\2cd\7\b\2\2de\5\6\4\2ef\5\24"+
		"\13\2fh\3\2\2\2gc\3\2\2\2hk\3\2\2\2ig\3\2\2\2ij\3\2\2\2jm\3\2\2\2ki\3"+
		"\2\2\2l`\3\2\2\2lm\3\2\2\2m\13\3\2\2\2nr\7\4\2\2oq\5\16\b\2po\3\2\2\2"+
		"qt\3\2\2\2rp\3\2\2\2rs\3\2\2\2su\3\2\2\2tr\3\2\2\2uv\5\26\f\2vw\7\5\2"+
		"\2w\r\3\2\2\2xy\7\23\2\2yz\5\6\4\2z\177\5\24\13\2{|\7\b\2\2|~\5\24\13"+
		"\2}{\3\2\2\2~\u0081\3\2\2\2\177}\3\2\2\2\177\u0080\3\2\2\2\u0080\u0082"+
		"\3\2\2\2\u0081\177\3\2\2\2\u0082\u0083\7\t\2\2\u0083\17\3\2\2\2\u0084"+
		"\u0085\7-\2\2\u0085\21\3\2\2\2\u0086\u0087\7-\2\2\u0087\23\3\2\2\2\u0088"+
		"\u0089\7-\2\2\u0089\25\3\2\2\2\u008a\u008c\5\30\r\2\u008b\u008a\3\2\2"+
		"\2\u008c\u008f\3\2\2\2\u008d\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e\27"+
		"\3\2\2\2\u008f\u008d\3\2\2\2\u0090\u0096\5\32\16\2\u0091\u0096\5\34\17"+
		"\2\u0092\u0096\5\36\20\2\u0093\u0096\5 \21\2\u0094\u0096\5\"\22\2\u0095"+
		"\u0090\3\2\2\2\u0095\u0091\3\2\2\2\u0095\u0092\3\2\2\2\u0095\u0093\3\2"+
		"\2\2\u0095\u0094\3\2\2\2\u0096\31\3\2\2\2\u0097\u0098\7\24\2\2\u0098\u009d"+
		"\5\24\13\2\u0099\u009a\7\25\2\2\u009a\u009b\5$\23\2\u009b\u009c\7\26\2"+
		"\2\u009c\u009e\3\2\2\2\u009d\u0099\3\2\2\2\u009d\u009e\3\2\2\2\u009e\u009f"+
		"\3\2\2\2\u009f\u00a0\7\27\2\2\u00a0\u00a1\5$\23\2\u00a1\u00a2\7\t\2\2"+
		"\u00a2\33\3\2\2\2\u00a3\u00a4\7\30\2\2\u00a4\u00a5\7\21\2\2\u00a5\u00a6"+
		"\5$\23\2\u00a6\u00a7\7\22\2\2\u00a7\u00a8\7\4\2\2\u00a8\u00a9\5\26\f\2"+
		"\u00a9\u00af\7\5\2\2\u00aa\u00ab\7\31\2\2\u00ab\u00ac\7\4\2\2\u00ac\u00ad"+
		"\5\26\f\2\u00ad\u00ae\7\5\2\2\u00ae\u00b0\3\2\2\2\u00af\u00aa\3\2\2\2"+
		"\u00af\u00b0\3\2\2\2\u00b0\35\3\2\2\2\u00b1\u00b2\7\32\2\2\u00b2\u00b3"+
		"\7\21\2\2\u00b3\u00b4\5$\23\2\u00b4\u00b5\7\22\2\2\u00b5\u00b6\7\4\2\2"+
		"\u00b6\u00b7\5\26\f\2\u00b7\u00b8\7\5\2\2\u00b8\37\3\2\2\2\u00b9\u00ba"+
		"\7\33\2\2\u00ba\u00bb\5(\25\2\u00bb\u00bc\7\t\2\2\u00bc!\3\2\2\2\u00bd"+
		"\u00bf\7\34\2\2\u00be\u00c0\5$\23\2\u00bf\u00be\3\2\2\2\u00bf\u00c0\3"+
		"\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c2\7\t\2\2\u00c2#\3\2\2\2\u00c3\u00c9"+
		"\5&\24\2\u00c4\u00c5\5,\27\2\u00c5\u00c6\5&\24\2\u00c6\u00c8\3\2\2\2\u00c7"+
		"\u00c4\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9\u00ca\3\2"+
		"\2\2\u00ca%\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cc\u00de\7+\2\2\u00cd\u00de"+
		"\7,\2\2\u00ce\u00de\5\60\31\2\u00cf\u00de\5\24\13\2\u00d0\u00d1\5\24\13"+
		"\2\u00d1\u00d2\7\25\2\2\u00d2\u00d3\5$\23\2\u00d3\u00d4\7\26\2\2\u00d4"+
		"\u00de\3\2\2\2\u00d5\u00de\5(\25\2\u00d6\u00d7\7\21\2\2\u00d7\u00d8\5"+
		"$\23\2\u00d8\u00d9\7\22\2\2\u00d9\u00de\3\2\2\2\u00da\u00db\5.\30\2\u00db"+
		"\u00dc\5&\24\2\u00dc\u00de\3\2\2\2\u00dd\u00cc\3\2\2\2\u00dd\u00cd\3\2"+
		"\2\2\u00dd\u00ce\3\2\2\2\u00dd\u00cf\3\2\2\2\u00dd\u00d0\3\2\2\2\u00dd"+
		"\u00d5\3\2\2\2\u00dd\u00d6\3\2\2\2\u00dd\u00da\3\2\2\2\u00de\'\3\2\2\2"+
		"\u00df\u00e0\5\22\n\2\u00e0\u00e1\7\21\2\2\u00e1\u00e2\5*\26\2\u00e2\u00e3"+
		"\7\22\2\2\u00e3\u00ef\3\2\2\2\u00e4\u00e7\5\20\t\2\u00e5\u00e7\5\24\13"+
		"\2\u00e6\u00e4\3\2\2\2\u00e6\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00e9"+
		"\7\35\2\2\u00e9\u00ea\5\22\n\2\u00ea\u00eb\7\21\2\2\u00eb\u00ec\5*\26"+
		"\2\u00ec\u00ed\7\22\2\2\u00ed\u00ef\3\2\2\2\u00ee\u00df\3\2\2\2\u00ee"+
		"\u00e6\3\2\2\2\u00ef)\3\2\2\2\u00f0\u00f5\5$\23\2\u00f1\u00f2\7\b\2\2"+
		"\u00f2\u00f4\5$\23\2\u00f3\u00f1\3\2\2\2\u00f4\u00f7\3\2\2\2\u00f5\u00f3"+
		"\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f9\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f8"+
		"\u00f0\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9+\3\2\2\2\u00fa\u00fb\t\4\2\2"+
		"\u00fb-\3\2\2\2\u00fc\u00fd\t\5\2\2\u00fd/\3\2\2\2\u00fe\u00ff\t\6\2\2"+
		"\u00ff\61\3\2\2\2\268>JSXilr\177\u008d\u0095\u009d\u00af\u00bf\u00c9\u00dd"+
		"\u00e6\u00ee\u00f5\u00f8";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}