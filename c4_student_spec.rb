#
# Harrison Corbin
#
require 'spec_helper'

describe 'C4 standard board size' do
    it 'detects P1 winning horizontally in row 0' do
        # Notice that the game should end before the last 'q' input is consumed
        result = test_c4('aabbccdq')
        expect(result).to declare_win_for 1
    end

    it 'quits before declaring a winner in column 0' do
        result = test_c4('abababq')
        expect(result).to be_abandoned
    end
end


describe 'Connect 4 alternate' do
    it 'detects player 2 winning horizontally on a big board' do
        result = test_c4('abbccdde', 6, 7, 4)
        expect(result).to declare_win_for 2
    end

    it 'quits before declaring p2 a winner horizontally' do
        result = test_c4('abbccddq', 6, 7, 4)
        expect(result).to be_abandoned
    end
end

describe 'Connect 4 alternate' do
    it 'detects player 1 winning vertically on a big board' do
        result = test_c4('abacadaq', 6, 7, 4)
        expect(result).to declare_win_for 1
    end

    it 'quits before declaring p1 a winner vertically' do
        result = test_c4('abacadq', 6, 7, 4)
        expect(result).to be_abandoned
    end
end

describe 'Connect 4 alternate' do
    it 'detects player 2 winning vertically on a big board' do
        result = test_c4('abcbcbcb', 6, 7, 4)
        expect(result).to declare_win_for 2
    end

    it 'quits before declaring p2 a winner vertically' do
        result = test_c4('abcbcbcq', 6, 7, 4)
        expect(result).to be_abandoned
    end
end

describe 'Connect 4 alternate' do
    it 'detects player 1 winning diagonally on a big board' do
        result = test_c4('abbccdedcddq', 6, 7, 4)
        expect(result).to declare_win_for 1
    end

    it 'quits before declaring p1 a winner diagonally' do
        result = test_c4('abbccdedcdq', 6, 7, 4)
        expect(result).to be_abandoned
    end
end

describe 'Connect 4 alternate' do
    it 'detects player 2 winning diagonally on a big board' do
        result = test_c4('abccbdddeeee', 6, 7, 4)
        expect(result).to declare_win_for 2
    end

    it 'quits before declaring p2 a winner diagonally' do
        result = test_c4('abccbdddeeeq', 6, 7, 4)
        expect(result).to be_abandoned
    end
end

describe 'Connect 4 alternate' do
    it 'detects a tie' do
        result = test_c4('aabbccaabbccaabbccedfegfdggdfgefdegdfgefde', 6, 7, 4)
    end

    it 'quits before declaring a winner tie' do
        result = test_c4('aabbccaabbccaabbccedfegfdggdfgefdegdfgefdq', 6, 7, 4)
        expect(result).to be_abandoned
    end
end
