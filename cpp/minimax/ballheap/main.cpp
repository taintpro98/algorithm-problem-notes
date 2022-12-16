#include <bits/stdc++.h>
using namespace std;

struct Move
{
    int mheap, nheap;
};

int m,
    n, k;
//computer is max
//player is min
bool isMoveLeft(pair<int, int> state)
{
    if (state.first == 0 && state.second == 0)
        return false;
    return true;
}

int minimax(pair<int, int> state, int depth, bool isMax)
{
    if (!isMoveLeft(state))
    {
        if (isMax)
            return -10;
        else
            return 10;
    }
    if (isMax)
    {
        int best = -1000;
        for (int i = 1; i <= min(k, state.first); i++)
        {
            // Make the move
            state.first = state.first - i;
            best = max(best, minimax(state, depth + 1, !isMax));

            // Undo the move
            state.first = state.first + i;
        }
        for (int j = 1; j <= min(k, state.second); j++)
        {
            // Make the move
            state.second = state.second - j;
            best = max(best, minimax(state, depth + 1, !isMax));

            // Undo the move
            state.second = state.second + j;
        }
        return best;
    }
    else
    {
        int best = 1000;
        for (int i = 1; i <= min(k, state.first); i++)
        {
            // Make the move
            state.first = state.first - i;
            best = min(best, minimax(state, depth + 1, !isMax));

            // Undo the move
            state.first = state.first + i;
        }
        for (int j = 1; j <= min(k, state.second); j++)
        {
            // Make the move
            state.second = state.second - j;
            best = min(best, minimax(state, depth + 1, !isMax));

            // Undo the move
            state.second = state.second + j;
        }
        return best;
    }
}

Move findBestMove(pair<int, int> state)
{
    Move bestMove;
    bestMove.mheap = -1;
    bestMove.nheap = -1;
    int bestVal = -1000;

    for (int i = 1; i <= min(k, state.first); i++)
    {
        // Make the move
        state.first = state.first - i;
        int moveVal = minimax(state, 0, false);

        // Undo the move
        state.first = state.first + i;
        if (moveVal > bestVal)
        {
            bestMove.mheap = i;
            bestMove.nheap = 0;
            bestVal = moveVal;
        }
    }
    for (int j = 1; j <= min(k, state.second); j++)
    {
        // Make the move
        state.second = state.second - j;
        int moveVal = minimax(state, 0, false);

        // Undo the move
        state.second = state.second + j;
        if (moveVal > bestVal)
        {
            bestMove.mheap = 0;
            bestMove.nheap = j;
            bestVal = moveVal;
        }
    }
    return bestMove;
}

pair<int, int> manipulate(pair<int, int> state, Move move){
    pair<int, int> newState = {state.first - move.mheap, state.second - move.nheap};
    return newState;
}

int main()
{
    m = 10;
    n = 8;
    k = 5;
    pair<int, int> state = {m, n};
    // Move bestMove = findBestMove(state);
    // printf("The Optimal Move is :\n");
	// printf("MHeap: %d NHeap: %d\n\n", bestMove.mheap, bestMove.nheap );

    printf("Current State: \n");
    printf("MHeap: %d NHeap: %d\n\n", state.first, state.second );
    while(true){
        printf("----------------------------------------------------\n");
        printf("Player types the move: ");
        int x, y; cin >> x >> y;
        Move playerMove;
        playerMove.mheap = x; playerMove.nheap = y;
        state = manipulate(state, playerMove);
        printf("Current state after player's turn: \n");
        printf("MHeap: %d NHeap: %d\n\n", state.first, state.second );

        Move bestMove = findBestMove(state);
        state = manipulate(state, bestMove);
        printf("Current state after computer's turn: \n");
        printf("MHeap: %d NHeap: %d\n\n", state.first, state.second );
        printf("----------------------------------------------------\n");
    }
    return 0;
}